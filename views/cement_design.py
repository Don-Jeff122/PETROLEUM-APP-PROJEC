import streamlit as st

from modules.database import (
    load_cement_database,
    get_cement_data
)

from modules.cement import (
    calculate_annular_volume,
    calculate_cement_sacks,
    validate_inputs
)


def show():

    st.title("🏗 Cement Design")

    st.write("Design a primary cement job.")

    # -----------------------------
    # Cement Database
    # -----------------------------
    database = load_cement_database()

    cement_class = st.selectbox(
        "Select Cement Class",
        database["Class"]
    )

    cement = get_cement_data(cement_class)

    st.subheader("Selected Cement Properties")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Density",
            f"{cement['Density_ppg']} ppg"
        )

        st.metric(
            "Yield",
            f"{cement['Yield_m3_per_sack']} m³/sack"
        )

    with col2:
        st.metric(
            "Maximum Temperature",
            f"{cement['Max_Temperature_C']} °C"
        )

        st.metric(
            "Recommended Use",
            cement["Recommended_Use"]
        )

    st.divider()

    # -----------------------------
    # User Inputs
    # -----------------------------
    hole_diameter = st.number_input(
        "Hole Diameter (in)",
        min_value=0.0,
        value=8.5
    )

    casing_od = st.number_input(
        "Casing Outside Diameter (in)",
        min_value=0.0,
        value=5.5
    )

    interval_length = st.number_input(
        "Cement Interval (m)",
        min_value=0.0,
        value=1000.0
    )

    excess_percent = st.number_input(
        "Excess (%)",
        min_value=0.0,
        value=15.0
    )

    if st.button("Calculate Cement Design"):

        yield_per_sack = cement["Yield_m3_per_sack"]

        valid, message = validate_inputs(
            hole_diameter,
            casing_od,
            interval_length,
            excess_percent,
            yield_per_sack
        )

        if not valid:
            st.error(message)
            return

        volume = calculate_annular_volume(
            hole_diameter,
            casing_od,
            interval_length,
            excess_percent
        )

        sacks = calculate_cement_sacks(
            volume,
            yield_per_sack
        )

        st.session_state["cement_results"] = {
            "Cement Class": cement_class,
            "Slurry Volume": volume,
            "Required Cement": sacks
        }

        st.divider()

        st.subheader("Results")

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                "Annular Volume",
                f"{volume:.2f} m³"
            )

        with result_col2:
            st.metric(
                "Required Cement",
                f"{sacks:.0f} sacks"
            )

        st.table({
            "Parameter": [
                "Cement Class",
                "Density",
                "Yield",
                "Maximum Temperature",
                "Recommended Use",
                "Hole Diameter",
                "Casing Outside Diameter",
                "Cement Interval",
                "Excess",
                "Annular Volume",
                "Required Cement"
            ],
            "Value": [
                cement_class,
                f"{cement['Density_ppg']} ppg",
                f"{yield_per_sack:.3f} m³/sack",
                f"{cement['Max_Temperature_C']} °C",
                cement["Recommended_Use"],
                f"{hole_diameter:.2f} in",
                f"{casing_od:.2f} in",
                f"{interval_length:.2f} m",
                f"{excess_percent:.2f} %",
                f"{volume:.2f} m³",
                f"{sacks:.0f} sacks"
            ]
        })

        st.success("Cement design completed successfully.")