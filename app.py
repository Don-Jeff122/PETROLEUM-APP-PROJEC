import mimetypes
from pathlib import Path

import streamlit as st

from views import (
    mud_weight,
    rheology,
    hydraulics,
    cement_design,
    plug_design,
    abandonment,
    results,
    about,
)
from modules.constants import APP_NAME, APP_TAGLINE, APP_VERSION, AUTHOR
from views.ui_style import inject_global_css, close_sidebar

# Serve .woff2 fonts with the correct content type (Windows mimetypes lacks it)
mimetypes.add_type("font/woff2", ".woff2")

st.set_page_config(
    page_title=APP_NAME,
    page_icon=":material/oil_barrel:",
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
            st.markdown(
                '<div class="logo-fallback"><span class="material-symbols-outlined">oil_barrel</span></div>',
                unsafe_allow_html=True,
            )

    with name_col:
        st.markdown(
            f"""
            <div class="sidebar-brand">
                <div class="app-name">{APP_NAME}</div>
                <div class="app-tagline">{APP_TAGLINE}</div>
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
            "Abandonment",
            "Results",
            "About",
        ],
        label_visibility="collapsed",
    )

    st.markdown(
        f"""
        <div class="sidebar-footer">
            <div class="version">Version {APP_VERSION}</div>
            <div class="author">{AUTHOR}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Auto-collapse the sidebar after navigating to a module
if (
    st.session_state.get("previous_page") is not None
    and st.session_state["previous_page"] != page
):
    close_sidebar()
st.session_state["previous_page"] = page

# ── Pages ────────────────────────────────────────────────────────────────────
if page == "Home":
    st.markdown(
        f"""
        <div class="home-hero">
            <h1><span class="material-symbols-outlined">oil_barrel</span> {APP_NAME}</h1>
            <p class="hero-sub">
                Integrated drilling fluid and cementing engineering platform
                for mud weight design, rheology, hydraulics, and cement job planning.
            </p>
            <div class="hero-badges">
                <span class="hero-badge">6 Engineering Modules</span>
                <span class="hero-badge">PDF Report Export</span>
                <span class="hero-badge">API Cement Database</span>
                <span class="hero-badge">Job Procedure Sheets</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Modules", "6", "Engineering tools")
    with col2:
        st.metric("Calculations", "6", "Core workflows")
    with col3:
        st.metric("Export", "PDF", "Reports & procedures")

    st.markdown(
        """
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon"><span class="material-symbols-outlined">oil_barrel</span></div>
                <h3>Mud Weight Design</h3>
                <p>Balance pore and fracture pressures with safe mud density windows.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon"><span class="material-symbols-outlined">science</span></div>
                <h3>Rheology Analysis</h3>
                <p>Bingham plastic model from viscometer readings with flow curves.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon"><span class="material-symbols-outlined">waves</span></div>
                <h3>Hydraulics</h3>
                <p>Annular velocity, pressure drops, ECD and hole cleaning evaluation.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon"><span class="material-symbols-outlined">construction</span></div>
                <h3>Cement Design</h3>
                <p>Primary cement job sizing with API database, additives and temperature checks.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon"><span class="material-symbols-outlined">block</span></div>
                <h3>Plug Design</h3>
                <p>Cement plug volume and sack requirements with depth tracking.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon"><span class="material-symbols-outlined">recycling</span></div>
                <h3>Plug &amp; Abandonment</h3>
                <p>Abandonment plugs, squeeze cement volumes and balanced plug design.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon"><span class="material-symbols-outlined">monitoring</span></div>
                <h3>Results Dashboard</h3>
                <p>Consolidated summary, PDF report export and cementing job procedure sheets.</p>
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

elif page == "Abandonment":
    abandonment.show()

elif page == "Results":
    results.show()

elif page == "About":
    about.show()
