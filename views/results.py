import streamlit as st

from modules.report import generate_report
from views.ui_style import page_header, section_title, progress_overview


def show():

    page_header(
        "📊",
        "Results Dashboard",
        "Consolidated summary of all engineering calculations.",
    )

    mud = st.session_state.get("mud_results")
    rheology = st.session_state.get("rheology_results")
    hydraulics = st.session_state.get("hydraulics_results")
    cement = st.session_state.get("cement_results")
    plug = st.session_state.get("plug_results")

    modules_status = [
        ("Mud Weight", mud is not None),
        ("Rheology", rheology is not None),
        ("Hydraulics", hydraulics is not None),
        ("Cement", cement is not None),
        ("Plug", plug is not None),
    ]
    completed = sum(1 for _, done in modules_status if done)

    progress_overview(completed, 5, modules_status)

    overview_col, status_col = st.columns([2, 1])
    with overview_col:
        st.metric("Calculations Complete", f"{completed} / 5")
    with status_col:
        st.metric("Report Status", "Ready" if completed else "Pending")

    st.divider()

    # ── Mud Weight ──
    with st.container(border=True):
        section_title("Module", "Mud Weight")
        if mud:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Mud Density", f"{mud['Mud Density']:.2f} kg/m³")
            with col2:
                st.metric("Hydrostatic Pressure", f"{mud['Hydrostatic Pressure']:.2f} MPa")
            with col3:
                st.metric("Min Safe Density", f"{mud['Minimum Safe Density']:.2f} kg/m³")
            with col4:
                st.metric("Max Safe Density", f"{mud['Maximum Safe Density']:.2f} kg/m³")
            if mud["Status"] == "SAFE":
                st.success(f"Status: {mud['Status']}")
            elif mud["Status"] == "TOO LOW":
                st.error(f"Status: {mud['Status']}")
            else:
                st.warning(f"Status: {mud['Status']}")
        else:
            st.info("No Mud Weight calculation available. Run the module from the sidebar.")

    # ── Rheology ──
    with st.container(border=True):
        section_title("Module", "Rheology")
        if rheology:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Plastic Viscosity", f"{rheology['Plastic Viscosity']:.2f} cP")
            with col2:
                st.metric("Yield Point", f"{rheology['Yield Point']:.2f} lb/100 ft²")
        else:
            st.info("No Rheology calculation available.")

    # ── Hydraulics ──
    with st.container(border=True):
        section_title("Module", "Hydraulics")
        if hydraulics:
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Annular Velocity", f"{hydraulics['Annular Velocity']:.2f} m/s")
            with col2:
                st.metric("Hole Cleaning", hydraulics["Hole Cleaning"])
        else:
            st.info("No Hydraulics calculation available.")

    # ── Cement Design ──
    with st.container(border=True):
        section_title("Module", "Cement Design")
        if cement:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Slurry Volume", f"{cement['Slurry Volume']:.2f} m³")
            with col2:
                st.metric("Required Cement", f"{cement['Required Cement']:.0f} sacks")
            with col3:
                st.metric("Cement Class", cement["Cement Class"])
        else:
            st.info("No Cement Design calculation available.")

    # ── Plug Design ──
    with st.container(border=True):
        section_title("Module", "Plug Design")
        if plug:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Plug Volume", f"{plug['Plug Volume']:.2f} m³")
            with col2:
                st.metric("Required Cement", f"{plug['Required Cement']:.0f} sacks")
            with col3:
                st.metric("Top of Plug", f"{plug['Top of Plug']:.2f} m")
            with col4:
                st.metric("Bottom of Plug", f"{plug['Bottom of Plug']:.2f} m")
        else:
            st.info("No Plug Design calculation available.")

    st.divider()

    # ── Export ──
    with st.container(border=True):
        section_title("Export", "Engineering Report")

        export_col, clear_col = st.columns(2)
        with export_col:
            generate = st.button("Generate PDF Report", use_container_width=True)
        with clear_col:
            clear = st.button("Clear All Results", use_container_width=True)

        if generate:
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
                generate_report(filename, sections)
                with open(filename, "rb") as pdf:
                    st.download_button(
                        label="Download PDF Report",
                        data=pdf,
                        file_name=filename,
                        mime="application/pdf",
                        use_container_width=True,
                    )

        if clear:
            keys = [
                "mud_results",
                "rheology_results",
                "hydraulics_results",
                "cement_results",
                "plug_results",
            ]
            for key in keys:
                if key in st.session_state:
                    del st.session_state[key]
            st.success("All saved results have been cleared.")
            st.rerun()
