from pathlib import Path

import streamlit as st

from views import plug_design
from views import (
    mud_weight,
    rheology,
    hydraulics,
    cement_design,
    results,
    about,
)
from views.ui_style import inject_global_css

st.set_page_config(
    page_title="PyMudCement-Optima",
    page_icon="🛢",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_global_css()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    logo_col, name_col = st.columns([1, 2.2], vertical_alignment="center")

    with logo_col:
        logo_path = Path("assets/JEFFY-LOGO.png")
        if logo_path.exists():
            st.image(str(logo_path), width=52)
        else:
            st.markdown('<div class="logo-fallback">🛢</div>', unsafe_allow_html=True)

    with name_col:
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="app-name">PyMudCement-Optima</div>
                <div class="app-tagline">Drilling &amp; Cementing Engineering</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown('<div class="nav-section-label">Navigation</div>', unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        [
            "Home",
            "Mud Weight",
            "Rheology",
            "Hydraulics",
            "Cement Design",
            "Plug Design",
            "Results",
            "About",
        ],
        label_visibility="collapsed",
    )

    st.markdown(
        """
        <div class="sidebar-footer">
            <div class="version">Version 1.0</div>
            <div class="author">Donkor Jeffery</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── Pages ────────────────────────────────────────────────────────────────────
if page == "Home":
    st.markdown(
        """
        <div class="home-hero">
            <h1>🛢 PyMudCement-Optima</h1>
            <p class="hero-sub">
                Integrated drilling fluid and cementing engineering platform
                for mud weight design, rheology, hydraulics, and cement job planning.
            </p>
            <div class="hero-badges">
                <span class="hero-badge">6 Engineering Modules</span>
                <span class="hero-badge">PDF Report Export</span>
                <span class="hero-badge">API Cement Database</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Modules", "6", "Engineering tools")
    with col2:
        st.metric("Calculations", "5", "Core workflows")
    with col3:
        st.metric("Export", "PDF", "Engineering reports")

    st.markdown(
        """
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">🛢</div>
                <h3>Mud Weight Design</h3>
                <p>Balance pore and fracture pressures with safe mud density windows.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🧪</div>
                <h3>Rheology Analysis</h3>
                <p>Bingham plastic model from viscometer readings with flow curves.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🌊</div>
                <h3>Hydraulics</h3>
                <p>Annular velocity and hole cleaning evaluation for optimal flow rates.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🏗</div>
                <h3>Cement Design</h3>
                <p>Primary cement job sizing with API cement class database.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🛑</div>
                <h3>Plug Design</h3>
                <p>Cement plug volume and sack requirements with depth tracking.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <h3>Results Dashboard</h3>
                <p>Consolidated summary and PDF report export for all calculations.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="home-callout">
            <strong>Getting started:</strong> Select a module from the sidebar to begin.
            Results are saved automatically and can be exported from the Results page.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Mud Weight":
    mud_weight.show()

elif page == "Rheology":
    rheology.show()

elif page == "Hydraulics":
    hydraulics.show()

elif page == "Cement Design":
    cement_design.show()

elif page == "Plug Design":
    plug_design.show()

elif page == "Results":
    results.show()

elif page == "About":
    about.show()
