import streamlit as st

from modules.rheology import (
    calculate_pv,
    calculate_yp,
    validate_inputs
)


def show():

    st.title("🧪 Mud Rheology")

    st.write("Enter the viscometer readings.")

    reading_600 = st.number_input(
        "600 RPM Reading",
        value=60.0
    )

    reading_300 = st.number_input(
        "300 RPM Reading",
        value=40.0
    )

    if st.button("Calculate Rheology"):

        valid, message = validate_inputs(
            reading_600,
            reading_300
        )

        if not valid:
            st.error(message)
            return

        pv = calculate_pv(
            reading_600,
            reading_300
        )

        yp = calculate_yp(
            reading_300,
            pv
        )

        st.session_state["rheology_results"] = {
            "Plastic Viscosity": pv,
            "Yield Point": yp
        }

        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Plastic Viscosity (PV)",
                f"{pv:.2f} cP"
            )

        with col2:

            st.metric(
                "Yield Point (YP)",
                f"{yp:.2f} lb/100 ft²"
            )

        st.divider()

        st.table({
            "Parameter": [
                "600 RPM Reading",
                "300 RPM Reading",
                "Plastic Viscosity",
                "Yield Point"
            ],
            "Value": [
                f"{reading_600:.2f}",
                f"{reading_300:.2f}",
                f"{pv:.2f} cP",
                f"{yp:.2f} lb/100 ft²"
            ]
        })

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