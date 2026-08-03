import streamlit as st

from modules.database import load_cement_database, get_cement_data
from modules.cement import (
    calculate_annular_volume,
    calculate_cement_sacks,
    validate_inputs,
)
from views.ui_style import page_header, section_title, results_table


def show():

    page_header(
        "🏗",
        "Cement Design",
        "Size a primary cement job using the API cement class database.",
    )

    database = load_cement_database()

    with st.container(border=True):
        section_title("Step 1", "Select Cement Class")
        cement_class = st.selectbox(
            "Cement Class",
            database["Class"],
            label_visibility="collapsed",
        )

    cement = get_cement_data(cement_class)

    with st.container(border=True):
        section_title("Properties", f"{cement_class} Specifications")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Density", f"{cement['Density_ppg']} ppg")
        with col2:
            st.metric("Yield", f"{cement['Yield_m3_per_sack']} m³/sack")
        with col3:
            st.metric("Max Temperature", f"{cement['Max_Temperature_C']} °C")
        with col4:
            st.metric("Recommended Use", cement["Recommended_Use"])

    input_col, info_col = st.columns([1.2, 1], gap="large")

    with input_col:
        with st.container(border=True):
            section_title("Step 2", "Well Geometry")

            hole_diameter = st.number_input(
                "Hole Diameter (in)",
                min_value=0.0,
                value=8.5,
            )
            casing_od = st.number_input(
                "Casing Outside Diameter (in)",
                min_value=0.0,
                value=5.5,
            )
            interval_length = st.number_input(
                "Cement Interval (m)",
                min_value=0.0,
                value=1000.0,
            )
            excess_percent = st.number_input(
                "Excess (%)",
                min_value=0.0,
                value=15.0,
            )

            calculate = st.button("Calculate Cement Design", use_container_width=True)

    with info_col:
        with st.container(border=True):
            section_title("Guide", "Volume Calculation")
            st.markdown(
                """
                Annular volume is calculated from hole and casing
                diameters over the cement interval, with excess
                applied for hole irregularities.

                **Required sacks** = Volume ÷ Yield per sack
                """
            )

    if calculate:

        yield_per_sack = cement["Yield_m3_per_sack"]

        valid, message = validate_inputs(
            hole_diameter,
            casing_od,
            interval_length,
            excess_percent,
            yield_per_sack,
        )

        if not valid:
            st.error(message)
            return

        volume = calculate_annular_volume(
            hole_diameter,
            casing_od,
            interval_length,
            excess_percent,
        )
        sacks = calculate_cement_sacks(volume, yield_per_sack)

        st.session_state["cement_results"] = {
            "Cement Class": cement_class,
            "Slurry Volume": volume,
            "Required Cement": sacks,
        }

        st.divider()
        section_title("Results", "Cement Job Summary")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Annular Volume", f"{volume:.2f} m³")
        with col2:
            st.metric("Required Cement", f"{sacks:.0f} sacks")

        with st.container(border=True):
            results_table(
                [
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
                    "Required Cement",
                ],
                [
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
                    f"{sacks:.0f} sacks",
                ],
            )

        st.success("Cement design completed successfully.")
