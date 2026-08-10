import streamlit as st

from modules.constants import APP_NAME, APP_VERSION, AUTHOR, UNIVERSITY, DEPARTMENT
from views.ui_style import page_header, section_title, icon


def show():

    page_header(
        "info",
        "About PyMudCement-Optima",
        "Drilling fluid and cementing engineering software.",
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            section_title("Overview", "About the Application")
            st.markdown(
                f"""
                **{APP_NAME}** is a drilling engineering application
                built to help engineers with mud design, rheology analysis,
                hydraulics calculations, cementing design, plug design, and
                plug &amp; abandonment operations.

                This was developed as a final year project using
                **Python** and **Streamlit**.
                """
            )

        with st.container(border=True):
            section_title("Technology", "Built With")
            tech_col1, tech_col2 = st.columns(2)
            with tech_col1:
                st.markdown("- **Python**")
                st.markdown("- **Streamlit**")
                st.markdown("- **Pandas**")
            with tech_col2:
                st.markdown("- **Plotly**")
                st.markdown("- **NumPy**")
                st.markdown("- **ReportLab**")

    with col2:
        with st.container(border=True):
            section_title("Modules", "Available Tools")
            st.markdown(
                f"""
                <div class="module-list">
                    <div class="module-item">
                        <div class="mi-icon">{icon("oil_barrel")}</div>
                        <div class="mi-name">Mud Weight Design</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">{icon("science")}</div>
                        <div class="mi-name">Rheology Analysis</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">{icon("waves")}</div>
                        <div class="mi-name">Hydraulics</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">{icon("construction")}</div>
                        <div class="mi-name">Cement Design</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">{icon("block")}</div>
                        <div class="mi-name">Plug Design</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">{icon("monitoring")}</div>
                        <div class="mi-name">Results Dashboard</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            f"""
            <div class="dev-card">
                <div class="dev-label">Developer</div>
                <div class="dev-name">{AUTHOR}</div>
                <div class="dev-detail">
                    BSc {DEPARTMENT}<br>
                    {UNIVERSITY}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.success(f"Version {APP_VERSION} — {APP_NAME}")
