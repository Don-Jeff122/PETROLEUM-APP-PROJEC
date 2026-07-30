import streamlit as st

from modules.hydraulics import (
    calculate_annular_velocity,
    evaluate_hole_cleaning,
    validate_inputs
)


def show():

    st.title("🌊 Hydraulics")

    st.write("Calculate annular velocity.")

    flow_rate = st.number_input(
        "Pump Rate (L/min)",
        value=1200.0
    )

    hole_diameter = st.number_input(
        "Hole Diameter (inches)",
        value=8.5
    )

    pipe_od = st.number_input(
        "Pipe Outside Diameter (inches)",
        value=5.0
    )

    if st.button("Calculate Hydraulics"):

        valid, message = validate_inputs(
            flow_rate,
            hole_diameter,
            pipe_od
        )

        if not valid:
            st.error(message)
            return

        velocity = calculate_annular_velocity(
            flow_rate,
            hole_diameter,
            pipe_od
        )

        cleaning = evaluate_hole_cleaning(
            velocity
        )

        st.session_state["hydraulics_results"] = {
            "Annular Velocity": velocity,
            "Hole Cleaning": cleaning
        }

        st.session_state["hydraulics_results"] = {
            "Annular Velocity": velocity,
            "Hole Cleaning": cleaning
        }

        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Annular Velocity",
                f"{velocity:.2f} m/s"
            )

        with col2:

            st.metric(
                "Hole Cleaning",
                cleaning
            )

        st.divider()

        if cleaning == "GOOD":
            st.success("Hole cleaning is good.")

        elif cleaning == "FAIR":
            st.warning("Hole cleaning is fair.")

        else:
            st.error("Hole cleaning is poor.")

        st.table({
            "Parameter": [
                "Pump Rate",
                "Hole Diameter",
                "Pipe Diameter",
                "Annular Velocity",
                "Hole Cleaning"
            ],
            "Value": [
                f"{flow_rate:.2f} L/min",
                f"{hole_diameter:.2f} in",
                f"{pipe_od:.2f} in",
                f"{velocity:.2f} m/s",
                cleaning
            ]
        })