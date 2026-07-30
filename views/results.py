import streamlit as st
from modules.report import generate_report


def show():

    st.title("📊 Results Dashboard")

    st.write("Summary of the latest engineering calculations.")

    # ==========================
    # Mud Weight
    # ==========================
    st.subheader("🛢 Mud Weight")

    mud = st.session_state.get("mud_results")

    if mud:

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Mud Density",
                f"{mud['Mud Density']:.2f} kg/m³"
            )

            st.metric(
                "Minimum Safe Density",
                f"{mud['Minimum Safe Density']:.2f} kg/m³"
            )

        with col2:
            st.metric(
                "Hydrostatic Pressure",
                f"{mud['Hydrostatic Pressure']:.2f} MPa"
            )

            st.metric(
                "Maximum Safe Density",
                f"{mud['Maximum Safe Density']:.2f} kg/m³"
            )

        st.success(f"Status: {mud['Status']}")

    else:
        st.info("No Mud Weight calculation available.")

    st.divider()

    # ==========================
    # Rheology
    # ==========================
    st.subheader("🧪 Rheology")

    rheology = st.session_state.get("rheology_results")

    if rheology:

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Plastic Viscosity",
                f"{rheology['Plastic Viscosity']:.2f} cP"
            )

        with col2:
            st.metric(
                "Yield Point",
                f"{rheology['Yield Point']:.2f} lb/100 ft²"
            )

    else:
        st.info("No Rheology calculation available.")

    st.divider()

    # ==========================
    # Hydraulics
    # ==========================
    st.subheader("🌊 Hydraulics")

    hydraulics = st.session_state.get("hydraulics_results")

    if hydraulics:

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Annular Velocity",
                f"{hydraulics['Annular Velocity']:.2f} m/s"
            )

        with col2:
            st.metric(
                "Hole Cleaning",
                hydraulics["Hole Cleaning"]
            )

    else:
        st.info("No Hydraulics calculation available.")

    st.divider()

    # ==========================
    # Cement Design
    # ==========================
    st.subheader("🏗 Cement Design")

    cement = st.session_state.get("cement_results")

    if cement:

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Slurry Volume",
                f"{cement['Slurry Volume']:.2f} m³"
            )

        with col2:
            st.metric(
                "Required Cement",
                f"{cement['Required Cement']:.0f} sacks"
            )

        st.write(f"**Cement Class:** {cement['Cement Class']}")

    else:
        st.info("No Cement Design calculation available.")

    st.divider()

    # ==========================
    # Plug Design
    # ==========================
    st.subheader("🛑 Plug Design")

    plug = st.session_state.get("plug_results")

    if plug:

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Plug Volume",
                f"{plug['Plug Volume']:.2f} m³"
            )

            st.metric(
                "Top of Plug",
                f"{plug['Top of Plug']:.2f} m"
            )

        with col2:
            st.metric(
                "Required Cement",
                f"{plug['Required Cement']:.0f} sacks"
            )

            st.metric(
                "Bottom of Plug",
                f"{plug['Bottom of Plug']:.2f} m"
            )

    else:
        st.info("No Plug Design calculation available.")

    st.divider()

    # ==========================
    # PDF Report
    # ==========================
    st.subheader("📄 Export Report")

    if st.button("Generate PDF Report"):

        sections = {}

        if "mud_results" in st.session_state:
            sections["Mud Weight"] = st.session_state["mud_results"]

        if "rheology_results" in st.session_state:
            sections["Rheology"] = st.session_state["rheology_results"]

        if "hydraulics_results" in st.session_state:
            sections["Hydraulics"] = st.session_state["hydraulics_results"]

        if "cement_results" in st.session_state:
            sections["Cement Design"] = st.session_state["cement_results"]

        if "plug_results" in st.session_state:
            sections["Plug Design"] = st.session_state["plug_results"]

        if len(sections) == 0:
            st.warning("No calculations available to export.")

        else:

            filename = "Engineering_Report.pdf"

            generate_report(
                filename,
                sections
            )

            with open(filename, "rb") as pdf:

                st.download_button(
                    label="⬇ Download PDF Report",
                    data=pdf,
                    file_name=filename,
                    mime="application/pdf"
                )

    st.divider()

    # ==========================
    # Clear Results
    # ==========================
    if st.button("🗑 Clear All Results"):

        keys = [
            "mud_results",
            "rheology_results",
            "hydraulics_results",
            "cement_results",
            "plug_results"
        ]

        for key in keys:
            if key in st.session_state:
                del st.session_state[key]

        st.success("All saved results have been cleared.")
        st.rerun()