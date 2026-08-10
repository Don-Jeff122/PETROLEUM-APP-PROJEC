import streamlit as st

from modules.database import load_cement_database, get_cement_data
from modules.plug import (
    calculate_plug_volume,
    validate_inputs,
)
from views.ui_style import (
    page_header,
    section_title,
    results_table,
    begin_calculation,
    calculated_button,
    save_calculation,
    results_current,
    clear_results_button,
)


def show():

    page_header(
        "block",
        "Plug Design",
        "Calculate cement plug volume, sack requirements, and depth placement.",
    )

    database = load_cement_database()

    with st.container(border=True, key="module-first-card"):
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
            section_title("Step 2", "Plug Geometry")

            hole_diameter = st.number_input("Hole Diameter (in)", value=8.5)
            plug_length = st.number_input("Plug Length (m)", value=100.0)
            plug_top = st.number_input("Top of Plug (m)", value=1500.0)

            inputs = {
                "Cement Class": cement_class,
                "Hole Diameter": hole_diameter,
                "Plug Length": plug_length,
                "Top of Plug": plug_top,
            }
            calculate = calculated_button(
                "Calculate Plug",
                "plug_results",
                "calculate_plug",
                inputs=inputs,
            )

    plug_bottom = plug_top + plug_length

    with info_col:
        with st.container(border=True):
            section_title("Preview", "Plug Placement")
            st.metric("Top of Plug", f"{plug_top:.0f} m")
            st.metric("Bottom of Plug", f"{plug_bottom:.0f} m")
            st.metric("Plug Length", f"{plug_length:.0f} m")

    if calculate or results_current("plug_results", inputs):
        if calculate:
            begin_calculation("Calculating Plug…")

            yield_per_sack = cement["Yield_m3_per_sack"]

            valid, message = validate_inputs(
                hole_diameter,
                plug_length,
                yield_per_sack,
            )

            if not valid:
                st.error(message)
                return

        yield_per_sack = cement["Yield_m3_per_sack"]
        volume = calculate_plug_volume(hole_diameter, plug_length)
        sacks = volume / yield_per_sack  # required cement sacks

        if calculate:
            save_calculation("plug_results", {
                "Plug Volume": volume,
                "Required Cement": sacks,
                "Top of Plug": plug_top,
                "Bottom of Plug": plug_bottom,
            }, inputs)

        st.divider()
        section_title("Results", "Plug Design Summary")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Plug Volume", f"{volume:.2f} m³")
        with col2:
            st.metric("Required Cement", f"{sacks:.0f} sacks")
        with col3:
            st.metric("Top of Plug", f"{plug_top:.2f} m")
        with col4:
            st.metric("Bottom of Plug", f"{plug_bottom:.2f} m")

        with st.container(border=True):
            results_table(
                [
                    "Cement Class",
                    "Hole Diameter",
                    "Plug Length",
                    "Top of Plug",
                    "Bottom of Plug",
                    "Plug Volume",
                    "Required Cement",
                ],
                [
                    cement_class,
                    f"{hole_diameter:.2f} in",
                    f"{plug_length:.2f} m",
                    f"{plug_top:.2f} m",
                    f"{plug_bottom:.2f} m",
                    f"{volume:.2f} m³",
                    f"{sacks:.0f} sacks",
                ],
            )

        st.success("Plug design completed successfully.")

        clear_results_button("plug_results")
