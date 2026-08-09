import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

from modules.hydraulics import (
    calculate_annular_velocity,
    calculate_pressure_drop,
    calculate_ecd,
    evaluate_hole_cleaning,
    validate_inputs,
)
from views.ui_style import (
    page_header,
    section_title,
    results_table,
    apply_plotly_style,
    begin_calculation,
    calculated_button,
)


def show():

    page_header(
        "waves",
        "Hydraulics",
        "Evaluate annular velocity, hole cleaning, and ECD.",
    )

    input_col, info_col = st.columns([1.2, 1], gap="large")

    with input_col:
        with st.container(border=True):
            section_title("Inputs", "Flow Parameters")

            flow_rate = st.number_input("Pump Rate (L/min)", min_value=0.0, value=1200.0)
            hole_diameter = st.number_input("Hole Diameter (inches)", min_value=0.0, value=8.5)
            pipe_od = st.number_input("Pipe Outside Diameter (inches)", min_value=0.0, value=5.0)
            tvd = st.number_input("True Vertical Depth (m)", min_value=0.0, value=2500.0)
            mud_density = st.number_input("Mud Density (kg/m³)", min_value=0.0, value=1200.0)
            pv = st.number_input("Plastic Viscosity (cP)", min_value=0.0, value=20.0)
            yp = st.number_input("Yield Point (lb/100ft²)", min_value=0.0, value=15.0)

            calculate = calculated_button(
                "Calculate Hydraulics", "hydraulics_results", "calculate_hydraulics"
            )

    with info_col:
        with st.container(border=True):
            section_title("Guide", "Hole Cleaning Criteria")
            st.markdown(
                """
                Annular velocity determines cuttings transport efficiency.

                | Rating | Velocity |
                |--------|----------|
                | **GOOD** | ≥ 1.0 m/s |
                | **FAIR** | 0.5 – 1.0 m/s |
                | **POOR** | < 0.5 m/s |

                **ECD** = Mud weight + Pressure loss / (g × TVD)
                """
            )

    if calculate:
        begin_calculation("Calculating Hydraulics…")

        valid, message = validate_inputs(flow_rate, hole_diameter, pipe_od, tvd)

        if not valid:
            st.error(message)
            return

        velocity = calculate_annular_velocity(flow_rate, hole_diameter, pipe_od)
        cleaning = evaluate_hole_cleaning(velocity)

        # calculate pressure drop and ECD
        pressure_drop = calculate_pressure_drop(
            flow_rate, hole_diameter, pipe_od, tvd, mud_density, pv, yp
        )
        ecd = calculate_ecd(mud_density, tvd, pressure_drop)

        st.session_state["hydraulics_results"] = {
            "Annular Velocity": velocity,
            "Hole Cleaning": cleaning,
            "Pressure Drop": pressure_drop / 1_000_000,  # convert to MPa
            "ECD": ecd,
        }

        st.divider()
        section_title("Analysis", "Hydraulics Profile")

        # plot velocity vs flow rate
        flow_rates = np.linspace(100, 2000, 50)
        velocities = []
        for rate in flow_rates:
            v = calculate_annular_velocity(rate, hole_diameter, pipe_od)
            velocities.append(v)

        hydraulics_data = pd.DataFrame({
            "Flow Rate": flow_rates,
            "Annular Velocity": velocities,
        })

        fig = px.line(
            hydraulics_data,
            x="Flow Rate",
            y="Annular Velocity",
            title="Flow Rate vs Annular Velocity",
        )
        fig.update_layout(
            xaxis_title="Flow Rate (L/min)",
            yaxis_title="Annular Velocity (m/s)",
        )
        st.plotly_chart(apply_plotly_style(fig), width="stretch")

        section_title("Results", "Hydraulics Summary")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Annular Velocity", f"{velocity:.2f} m/s")
        with col2:
            st.metric("Hole Cleaning", cleaning)
        with col3:
            st.metric("Pressure Drop", f"{pressure_drop/1_000_000:.2f} MPa")
        with col4:
            st.metric("ECD", f"{ecd:.2f} kg/m³")

        if cleaning == "GOOD":
            st.success("Hole cleaning is good.")
        elif cleaning == "FAIR":
            st.warning("Hole cleaning is fair.")
        else:
            st.error("Hole cleaning is poor.")

        with st.container(border=True):
            results_table(
                [
                    "Pump Rate",
                    "Hole Diameter",
                    "Pipe Diameter",
                    "Annular Velocity",
                    "Hole Cleaning",
                    "Pressure Drop",
                    "ECD",
                ],
                [
                    f"{flow_rate:.2f} L/min",
                    f"{hole_diameter:.2f} in",
                    f"{pipe_od:.2f} in",
                    f"{velocity:.2f} m/s",
                    cleaning,
                    f"{pressure_drop/1_000_000:.2f} MPa",
                    f"{ecd:.2f} kg/m³",
                ],
            )
