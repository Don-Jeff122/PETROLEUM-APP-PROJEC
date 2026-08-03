import streamlit as st

from views.ui_style import page_header, section_title


def show():

    page_header(
        "ℹ",
        "About PyMudCement-Optima",
        "Drilling fluid and cementing engineering software.",
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            section_title("Overview", "About the Application")
            st.markdown(
                """
                **PyMudCement-Optima** is a drilling engineering application
                developed to assist engineers in mud design, rheology analysis,
                hydraulics calculations, cementing design, and plug design.

                The software was developed as a final year project using
                **Python** and **Streamlit**.
                """
            )

        with st.container(border=True):
            section_title("Technology", "Built With")
            tech_col1, tech_col2 = st.columns(2)
            with tech_col1:
                st.markdown("- **Python**")
                st.markdown("- **Streamlit**")
            with tech_col2:
                st.markdown("- **Pandas**")
                st.markdown("- **Plotly**")

    with col2:
        with st.container(border=True):
            section_title("Modules", "Available Tools")
            st.markdown(
                """
                <div class="module-list">
                    <div class="module-item">
                        <div class="mi-icon">🛢</div>
                        <div class="mi-name">Mud Weight Design</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">🧪</div>
                        <div class="mi-name">Rheology Analysis</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">🌊</div>
                        <div class="mi-name">Hydraulics</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">🏗</div>
                        <div class="mi-name">Cement Design</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">🛑</div>
                        <div class="mi-name">Plug Design</div>
                    </div>
                    <div class="module-item">
                        <div class="mi-icon">📊</div>
                        <div class="mi-name">Results Dashboard</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            """
            <div class="dev-card">
                <div class="dev-label">Developer</div>
                <div class="dev-name">Donkor Jeffery</div>
                <div class="dev-detail">
                    BSc Electrical and Electronic Engineering<br>
                    University of Energy and Natural Resources (UENR)
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.success("Version 1.0 — PyMudCement-Optima")
