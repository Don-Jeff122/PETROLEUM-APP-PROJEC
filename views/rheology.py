import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd

from modules.rheology import calculate_pv, calculate_yp, validate_inputs
from views.ui_style import page_header, section_title, results_table, apply_plotly_style


def show():

    page_header(
        "🧪",
        "Mud Rheology",
        "Analyse viscometer readings using the Bingham plastic model.",
    )

    input_col, info_col = st.columns([1.2, 1], gap="large")

    with input_col:
        with st.container(border=True):
            section_title("Inputs", "Viscometer Readings")

            reading_600 = st.number_input("600 RPM Reading", value=60.0)
            reading_300 = st.number_input("300 RPM Reading", value=40.0)

            calculate = st.button("Calculate Rheology", width="stretch")

    with info_col:
        with st.container(border=True):
            section_title("Guide", "Bingham Plastic Model")
            st.markdown(
                """
                **Plastic Viscosity (PV)** = R600 − R300

                **Yield Point (YP)** = R300 − PV

                | Parameter | Typical Range |
                |-----------|---------------|
                | PV | 10 – 40 cP |
                | YP | 15 – 30 lb/100 ft² |
                """
            )

    if calculate:

        valid, message = validate_inputs(reading_600, reading_300)

        if not valid:
            st.error(message)
            return

        pv = calculate_pv(reading_600, reading_300)
        yp = calculate_yp(reading_300, pv)

        st.session_state["rheology_results"] = {
            "Plastic Viscosity": pv,
            "Yield Point": yp,
        }

        st.divider()
        section_title("Analysis", "Shear Stress vs Shear Rate")

        shear_rate = np.linspace(1, 1000, 100)
        shear_stress = yp + pv * shear_rate / 100

        data = pd.DataFrame({
            "Shear Rate": shear_rate,
            "Shear Stress": shear_stress,
        })

        fig = px.line(
            data,
            x="Shear Rate",
            y="Shear Stress",
            title="Bingham Plastic Flow Curve",
        )
        fig.update_layout(
            xaxis_title="Shear Rate (s⁻¹)",
            yaxis_title="Shear Stress (Pa)",
        )
        st.plotly_chart(apply_plotly_style(fig), width="stretch")

        section_title("Results", "Rheology Summary")

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Plastic Viscosity (PV)", f"{pv:.2f} cP")
        with col2:
            st.metric("Yield Point (YP)", f"{yp:.2f} lb/100 ft²")

        with st.container(border=True):
            results_table(
                [
                    "600 RPM Reading",
                    "300 RPM Reading",
                    "Plastic Viscosity",
                    "Yield Point",
                ],
                [
                    f"{reading_600:.2f}",
                    f"{reading_300:.2f}",
                    f"{pv:.2f} cP",
                    f"{yp:.2f} lb/100 ft²",
                ],
            )

        if pv < 10:
            st.warning("Plastic Viscosity is low.")
        elif pv > 40:
            st.warning("Plastic Viscosity is high.")
        else:
            st.success("Plastic Viscosity is within a typical operating range.")

        if yp < 15:
            st.warning("Yield Point is low. Hole cleaning may be poor.")
        elif yp > 30:
            st.warning("Yield Point is high. Pump pressure may increase.")
        else:
            st.success("Yield Point is within a typical operating range.")
