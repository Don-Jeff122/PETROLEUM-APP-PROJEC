import streamlit as st

from modules.mud import (
    calculate_mud_density,
    calculate_hydrostatic_pressure,
    safe_window,
    check_safe_density,
    validate_inputs,
    pa_to_mpa
)


def show():

    st.title("🛢 Mud Weight Design")

    st.write("Enter the well information below.")

    pressure_unit = st.selectbox(
        "Pressure Unit",
        ["MPa", "Pa"]
    )

    if pressure_unit == "MPa":

        pore_pressure = st.number_input(
            "Formation Pore Pressure (MPa)",
            value=25.0
        )

        fracture_pressure = st.number_input(
            "Formation Fracture Pressure (MPa)",
            value=30.0
        )

        pore_pressure *= 1_000_000
        fracture_pressure *= 1_000_000

    else:

        pore_pressure = st.number_input(
            "Formation Pore Pressure (Pa)",
            value=25000000.0
        )

        fracture_pressure = st.number_input(
            "Formation Fracture Pressure (Pa)",
            value=30000000.0
        )

    tvd = st.number_input(
        "True Vertical Depth (m)",
        value=2500.0
    )

    if st.button("Calculate"):

        valid, message = validate_inputs(
            pore_pressure,
            fracture_pressure,
            tvd
        )

        if not valid:
            st.error(message)
            return

        mud_density = calculate_mud_density(
            pore_pressure,
            tvd
        )

        hydrostatic_pressure = calculate_hydrostatic_pressure(
            mud_density,
            tvd
        )

        minimum_density, maximum_density = safe_window(
            pore_pressure,
            fracture_pressure,
            tvd
        )

        status = check_safe_density(
            mud_density,
            minimum_density,
            maximum_density
        )

        st.session_state["mud_results"] = {
            "Mud Density": mud_density,
            "Hydrostatic Pressure": pa_to_mpa(hydrostatic_pressure),
            "Minimum Safe Density": minimum_density,
            "Maximum Safe Density": maximum_density,
            "Status": status
        }

        st.subheader("Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Mud Density",
                f"{mud_density:.2f} kg/m³"
            )

            st.metric(
                "Hydrostatic Pressure",
                f"{pa_to_mpa(hydrostatic_pressure):.2f} MPa"
            )

        with col2:
            st.metric(
                "Minimum Safe Density",
                f"{minimum_density:.2f} kg/m³"
            )

            st.metric(
                "Maximum Safe Density",
                f"{maximum_density:.2f} kg/m³"
            )

        st.divider()

        if status == "SAFE":
            st.success("Mud weight is within the safe operating window.")

        elif status == "TOO LOW":
            st.error("Mud weight is too low. There is a risk of a well kick.")

        else:
            st.warning("Mud weight is too high. There is a risk of formation fracture.")

        st.table({
            "Parameter": [
                "Pore Pressure",
                "Fracture Pressure",
                "True Vertical Depth",
                "Mud Density",
                "Hydrostatic Pressure",
                "Status"
            ],
            "Value": [
                f"{pa_to_mpa(pore_pressure):.2f} MPa",
                f"{pa_to_mpa(fracture_pressure):.2f} MPa",
                f"{tvd:.2f} m",
                f"{mud_density:.2f} kg/m³",
                f"{pa_to_mpa(hydrostatic_pressure):.2f} MPa",
                status
            ]
        })
