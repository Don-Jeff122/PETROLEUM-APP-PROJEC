import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

from modules.mud import (
    calculate_mud_density,
    calculate_hydrostatic_pressure,
    safe_window,
    check_safe_density,
    validate_inputs,
)
from modules.constants import GRAVITY, PA_PER_MPA
from views.ui_style import (
    page_header,
    section_title,
    results_table,
    apply_plotly_style,
    begin_calculation,
    calculated_button,
    save_calculation,
    results_current,
    clear_results_button,
)

# simple unit conversion
pa_to_mpa = lambda x: x / PA_PER_MPA


def show():

    page_header(
        "oil_barrel",
        "Mud Weight Design",
        "Calculate required mud density and verify the safe operating window.",
    )

    input_col, info_col = st.columns([1.2, 1], gap="large")

    with input_col:
        with st.container(border=True, key="module-first-card"):
            section_title("Inputs", "Well Parameters")

            pressure_unit = st.selectbox(
                "Pressure Unit",
                ["MPa", "Pa"],
            )

            if pressure_unit == "MPa":
                pore_pressure = st.number_input(
                    "Formation Pore Pressure (MPa)",
                    value=25.0,
                )
                fracture_pressure = st.number_input(
                    "Formation Fracture Pressure (MPa)",
                    value=30.0,
                )
                pore_pressure *= 1_000_000
                fracture_pressure *= 1_000_000
            else:
                pore_pressure = st.number_input(
                    "Formation Pore Pressure (Pa)",
                    value=25000000.0,
                )
                fracture_pressure = st.number_input(
                    "Formation Fracture Pressure (Pa)",
                    value=30000000.0,
                )

            tvd = st.number_input(
                "True Vertical Depth (m)",
                value=2500.0,
            )

            inputs = {
                "Pressure Unit": pressure_unit,
                "Pore Pressure": pore_pressure,
                "Fracture Pressure": fracture_pressure,
                "TVD": tvd,
            }
            calculate = calculated_button(
                "Calculate Mud Weight",
                "mud_results",
                "calculate_mud_weight",
                inputs=inputs,
            )

    with info_col:
        with st.container(border=True):
            section_title("Guide", "Safe Mud Weight Window")
            st.markdown(
                """
                The **safe mud weight window** lies between the minimum
                density required to control formation pressure and the maximum
                density before fracturing the formation.

                | Status | Meaning |
                |--------|---------|
                | **SAFE** | Within operating window |
                | **TOO LOW** | Kick risk |
                | **TOO HIGH** | Fracture risk |
                """
            )

    if calculate or results_current("mud_results", inputs):
        if calculate:
            begin_calculation("Calculating Mud Weight…")

            valid, message = validate_inputs(
                pore_pressure,
                fracture_pressure,
                tvd,
            )

            if not valid:
                st.error(message)
                return

        mud_density = calculate_mud_density(pore_pressure, tvd)
        hydrostatic_pressure = calculate_hydrostatic_pressure(mud_density, tvd)
        minimum_density, maximum_density = safe_window(
            pore_pressure, fracture_pressure, tvd
        )
        status = check_safe_density(mud_density, minimum_density, maximum_density)

        if calculate:
            save_calculation("mud_results", {
                "Mud Density": mud_density,
                "Hydrostatic Pressure": pa_to_mpa(hydrostatic_pressure),
                "Minimum Safe Density": minimum_density,
                "Maximum Safe Density": maximum_density,
                "Status": status,
            }, inputs)

        st.divider()
        section_title("Analysis", "Pressure Profile")

        depth = np.linspace(0, tvd, 100)
        mud_pressure = (mud_density * GRAVITY * depth) / PA_PER_MPA
        minimum_pressure = (minimum_density * GRAVITY * depth) / PA_PER_MPA
        maximum_pressure = (maximum_density * GRAVITY * depth) / PA_PER_MPA

        pressure_data = pd.DataFrame({
            "Depth": depth,
            "Mud Pressure": mud_pressure,
            "Minimum Pressure": minimum_pressure,
            "Maximum Pressure": maximum_pressure,
        })

        fig = px.line(
            pressure_data,
            x="Depth",
            y=["Mud Pressure", "Minimum Pressure", "Maximum Pressure"],
            title="Pressure vs Depth",
        )
        fig.update_layout(yaxis_title="Pressure (MPa)", xaxis_title="Depth (m)")
        st.plotly_chart(apply_plotly_style(fig), width="stretch")

        section_title("Results", "Mud Weight Summary")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Mud Density", f"{mud_density:.2f} kg/m³")
        with col2:
            st.metric("Hydrostatic Pressure", f"{pa_to_mpa(hydrostatic_pressure):.2f} MPa")
        with col3:
            st.metric("Min Safe Density", f"{minimum_density:.2f} kg/m³")
        with col4:
            st.metric("Max Safe Density", f"{maximum_density:.2f} kg/m³")

        if status == "SAFE":
            st.success("Mud weight is within the safe operating window.")
        elif status == "TOO LOW":
            st.error("Mud weight is too low. There is a risk of a well kick.")
        else:
            st.warning("Mud weight is too high. There is a risk of formation fracture.")

        with st.container(border=True):
            results_table(
                [
                    "Pore Pressure",
                    "Fracture Pressure",
                    "True Vertical Depth",
                    "Mud Density",
                    "Hydrostatic Pressure",
                    "Status",
                ],
                [
                    f"{pa_to_mpa(pore_pressure):.2f} MPa",
                    f"{pa_to_mpa(fracture_pressure):.2f} MPa",
                    f"{tvd:.2f} m",
                    f"{mud_density:.2f} kg/m³",
                    f"{pa_to_mpa(hydrostatic_pressure):.2f} MPa",
                    status,
                ],
            )

        clear_results_button("mud_results")
