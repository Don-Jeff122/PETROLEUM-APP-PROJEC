import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

from modules.hydraulics import (
    calculate_annular_velocity,
    evaluate_hole_cleaning,
    validate_inputs,
)
from views.ui_style import page_header, section_title, results_table, apply_plotly_style


def show():

    page_header(
        "🌊",
        "Hydraulics",
        "Evaluate annular velocity and hole cleaning performance.",
    )

    input_col, info_col = st.columns([1.2, 1], gap="large")

    with input_col:
        with st.container(border=True):
            section_title("Inputs", "Flow Parameters")

            flow_rate = st.number_input("Pump Rate (L/min)", value=1200.0)
            hole_diameter = st.number_input("Hole Diameter (inches)", value=8.5)
            pipe_od = st.number_input("Pipe Outside Diameter (inches)", value=5.0)

            calculate = st.button("Calculate Hydraulics", use_container_width=True)

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
                """
            )

    if calculate:

        valid, message = validate_inputs(flow_rate, hole_diameter, pipe_od)

        if not valid:
            st.error(message)
            return

        velocity = calculate_annular_velocity(flow_rate, hole_diameter, pipe_od)
        cleaning = evaluate_hole_cleaning(velocity)

        st.session_state["hydraulics_results"] = {
            "Annular Velocity": velocity,
            "Hole Cleaning": cleaning,
        }

        st.divider()
        section_title("Analysis", "Hydraulics Profile")

        flow_rates = np.linspace(100, 1000, 50)
        velocities = []

        for rate in flow_rates:
            velocity_point = rate / 1000
            velocities.append(velocity_point)

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
        st.plotly_chart(apply_plotly_style(fig), use_container_width=True)

        section_title("Results", "Hydraulics Summary")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Annular Velocity", f"{velocity:.2f} m/s")
        with col2:
            st.metric("Hole Cleaning", cleaning)

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
                ],
                [
                    f"{flow_rate:.2f} L/min",
                    f"{hole_diameter:.2f} in",
                    f"{pipe_od:.2f} in",
                    f"{velocity:.2f} m/s",
                    cleaning,
                ],
            )
