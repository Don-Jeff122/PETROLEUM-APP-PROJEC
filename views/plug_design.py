import streamlit as st

from modules.database import (
    load_cement_database,
    get_cement_data
)

from modules.plug import (
    calculate_plug_volume,
    calculate_cement_sacks,
    validate_inputs
)


def show():

    st.title("🛑 Plug Design")

    database = load_cement_database()

    cement_class = st.selectbox(
        "Select Cement Class",
        database["Class"]
    )

    cement = get_cement_data(cement_class)

    st.subheader("Selected Cement")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Density", f"{cement['Density_ppg']} ppg")
        st.metric("Yield", f"{cement['Yield_m3_per_sack']} m³/sack")

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

    hole_diameter = st.number_input(
        "Hole Diameter (in)",
        value=8.5
    )

    plug_length = st.number_input(
        "Plug Length (m)",
        value=100.0
    )

    plug_top = st.number_input(
        "Top of Plug (m)",
        value=1500.0
    )

    plug_bottom = plug_top + plug_length

    if st.button("Calculate Plug"):

        yield_per_sack = cement["Yield_m3_per_sack"]

        valid, message = validate_inputs(
            hole_diameter,
            plug_length,
            yield_per_sack
        )

        if not valid:
            st.error(message)
            return

        volume = calculate_plug_volume(
            hole_diameter,
            plug_length
        )

        sacks = calculate_cement_sacks(
            volume,
            yield_per_sack
        )

        st.session_state["plug_results"] = {
            "Plug Volume": volume,
            "Required Cement": sacks,
            "Top of Plug": plug_top,
            "Bottom of Plug": plug_bottom
        }

        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Plug Volume",
                f"{volume:.2f} m³"
            )

            st.metric(
                "Required Cement",
                f"{sacks:.0f} sacks"
            )

        with col2:
            st.metric(
                "Top of Plug",
                f"{plug_top:.2f} m"
            )

            st.metric(
                "Bottom of Plug",
                f"{plug_bottom:.2f} m"
            )

        st.table({
            "Parameter": [
                "Cement Class",
                "Hole Diameter",
                "Plug Length",
                "Top of Plug",
                "Bottom of Plug",
                "Plug Volume",
                "Required Cement"
            ],
            "Value": [
                cement_class,
                f"{hole_diameter:.2f} in",
                f"{plug_length:.2f} m",
                f"{plug_top:.2f} m",
                f"{plug_bottom:.2f} m",
                f"{volume:.2f} m³",
                f"{sacks:.0f} sacks"
            ]
        })

        st.success("Plug design completed successfully.")