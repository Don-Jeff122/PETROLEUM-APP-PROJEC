import streamlit as st

from modules.constants import PPG_TO_KG_M3
from modules.database import load_cement_database, get_cement_data
from modules.abandonment import (
    calculate_plug_volume,
    calculate_squeeze_volume,
    calculate_balanced_plug,
    calculate_abandonment_sacks,
    validate_inputs,
)
from views.ui_style import (
    page_header,
    section_title,
    results_table,
    begin_calculation,
    calculated_button,
)


def show():

    page_header(
        "recycling",
        "Plug & Abandonment",
        "Design abandonment cement plugs, squeeze volumes, and balanced plugs for P&A operations.",
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
            section_title("Step 2", "P&A Well Data")

            hole_diameter = st.number_input(
                "Hole / Casing Inside Diameter (in)",
                min_value=0.0,
                value=8.5,
            )
            plug_top = st.number_input("Top of Abandonment Plug (m)", value=1500.0)
            plug_length = st.number_input("Abandonment Plug Length (m)", min_value=0.0, value=100.0)
            squeeze_interval = st.number_input(
                "Squeeze Interval Length (m)",
                min_value=0.0,
                value=50.0,
            )
            squeeze_efficiency = st.slider(
                "Squeeze Efficiency",
                min_value=0.5,
                max_value=1.0,
                value=0.8,
                step=0.05,
                help="Fraction of the interval filled during squeeze cementing.",
            )
            mud_weight = st.number_input(
                "Mud Weight in Hole (kg/m³)",
                min_value=0.0,
                value=1200.0,
            )

            calculate = calculated_button(
                "Calculate Abandonment Design", "abandonment_results", "calculate_abandonment"
            )

    with info_col:
        with st.container(border=True):
            section_title("Guide", "P&A Plug Rules of Thumb")
            st.markdown(
                """
                Abandonment plugs are typically set:
                - **100–200 m** of cement above and below
                  each zone of interest
                - A **surface plug** below ground level
                - Squeeze cement into perforations using
                  70–90% efficiency assumptions

                **Balanced plug** — length is the difference
                between plug top and bottom depths.
                """
            )

    plug_bottom = plug_top + plug_length

    if calculate:
        begin_calculation("Calculating Abandonment Design…")

        yield_per_sack = cement["Yield_m3_per_sack"]

        valid, message = validate_inputs(hole_diameter, plug_length, yield_per_sack)
        if not valid:
            st.error(message)
            return

        # abandonment plug
        plug_volume = calculate_plug_volume(hole_diameter, plug_length)
        plug_sacks = calculate_abandonment_sacks(plug_volume, yield_per_sack)

        # squeeze cement
        squeeze_volume = calculate_squeeze_volume(
            hole_diameter, squeeze_interval, squeeze_efficiency
        )
        squeeze_sacks = calculate_abandonment_sacks(squeeze_volume, yield_per_sack)

        # balanced plug (cement column hydrostatics)
        cement_density = cement["Density_ppg"] * PPG_TO_KG_M3
        balanced_length, balanced_pressure = calculate_balanced_plug(
            plug_top, plug_bottom, mud_weight, cement_density
        )

        total_volume = plug_volume + squeeze_volume
        total_sacks = plug_sacks + squeeze_sacks

        st.session_state["abandonment_results"] = {
            "Cement Class": cement_class,
            "Plug Volume": plug_volume,
            "Plug Cement (sacks)": plug_sacks,
            "Squeeze Volume": squeeze_volume,
            "Squeeze Cement (sacks)": squeeze_sacks,
            "Total Volume": total_volume,
            "Total Cement (sacks)": total_sacks,
            "Top of Plug": plug_top,
            "Bottom of Plug": plug_bottom,
            "Balanced Plug Pressure (MPa)": balanced_pressure / 1_000_000,
        }

        st.divider()
        section_title("Results", "Abandonment Design Summary")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Plug Volume", f"{plug_volume:.2f} m³")
        with col2:
            st.metric("Plug Cement", f"{plug_sacks:.0f} sacks")
        with col3:
            st.metric("Squeeze Volume", f"{squeeze_volume:.2f} m³")
        with col4:
            st.metric("Squeeze Cement", f"{squeeze_sacks:.0f} sacks")

        col5, col6 = st.columns(2)
        with col5:
            st.metric("Total Cement", f"{total_sacks:.0f} sacks")
        with col6:
            st.metric("Balanced Plug Pressure", f"{balanced_pressure/1_000_000:.2f} MPa")

        if balanced_length != plug_length:
            st.info(
                "Balanced plug length derived from top/bottom depths. "
                "Verify the cement column height against the calculated plug volume."
            )

        with st.container(border=True):
            results_table(
                [
                    "Cement Class",
                    "Hole / Casing ID",
                    "Top of Plug",
                    "Bottom of Plug",
                    "Plug Length",
                    "Plug Volume",
                    "Plug Cement",
                    "Squeeze Interval",
                    "Squeeze Efficiency",
                    "Squeeze Volume",
                    "Squeeze Cement",
                    "Total Cement",
                    "Balanced Plug Pressure",
                ],
                [
                    cement_class,
                    f"{hole_diameter:.2f} in",
                    f"{plug_top:.2f} m",
                    f"{plug_bottom:.2f} m",
                    f"{plug_length:.2f} m",
                    f"{plug_volume:.2f} m³",
                    f"{plug_sacks:.0f} sacks",
                    f"{squeeze_interval:.2f} m",
                    f"{squeeze_efficiency:.0%}",
                    f"{squeeze_volume:.2f} m³",
                    f"{squeeze_sacks:.0f} sacks",
                    f"{total_sacks:.0f} sacks",
                    f"{balanced_pressure/1_000_000:.2f} MPa",
                ],
            )

        st.success("Abandonment design completed successfully.")
