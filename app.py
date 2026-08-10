import mimetypes

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
from views.ui_style import (
    inject_global_css,
    close_sidebar,
    bind_feature_cards,
    render_top_bar,
    icon,
)

# Serve .woff2 fonts with the correct content type (Windows mimetypes lacks it)
mimetypes.add_type("font/woff2", ".woff2")

st.set_page_config(
    page_title=APP_NAME,
    page_icon=":material/oil_barrel:",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_global_css()
render_top_bar()

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
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
            <h1>{icon("oil_barrel")} {APP_NAME}</h1>
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

    st.markdown(
        """
        <div class="home-stats">
            <div class="home-stat">
                <div class="hs-label">Modules</div>
                <div class="hs-value">6</div>
                <div class="hs-delta">Engineering tools</div>
            </div>
            <div class="home-stat">
                <div class="hs-label">Calculations</div>
                <div class="hs-value">6</div>
                <div class="hs-delta">Core workflows</div>
            </div>
            <div class="home-stat">
                <div class="hs-label">Export</div>
                <div class="hs-value">PDF</div>
                <div class="hs-delta">Reports &amp; procedures</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="feature-grid">
            <div class="feature-card" data-page="Mud Weight">
                <div class="feature-head">
                    <div class="feature-icon">{icon("oil_barrel")}</div>
                    <h3>Mud Weight Design</h3>
                </div>
                <p>Balance pore and fracture pressures with safe mud density windows.</p>
            </div>
            <div class="feature-card" data-page="Rheology">
                <div class="feature-head">
                    <div class="feature-icon">{icon("science")}</div>
                    <h3>Rheology Analysis</h3>
                </div>
                <p>Bingham plastic model from viscometer readings with flow curves.</p>
            </div>
            <div class="feature-card" data-page="Hydraulics">
                <div class="feature-head">
                    <div class="feature-icon">{icon("waves")}</div>
                    <h3>Hydraulics</h3>
                </div>
                <p>Annular velocity, pressure drops, ECD and hole cleaning evaluation.</p>
            </div>
            <div class="feature-card" data-page="Cement Design">
                <div class="feature-head">
                    <div class="feature-icon">{icon("construction")}</div>
                    <h3>Cement Design</h3>
                </div>
                <p>Primary cement job sizing with API database, additives and temperature checks.</p>
            </div>
            <div class="feature-card" data-page="Plug Design">
                <div class="feature-head">
                    <div class="feature-icon">{icon("block")}</div>
                    <h3>Plug Design</h3>
                </div>
                <p>Cement plug volume and sack requirements with depth tracking.</p>
            </div>
            <div class="feature-card" data-page="Abandonment">
                <div class="feature-head">
                    <div class="feature-icon">{icon("recycling")}</div>
                    <h3>Plug &amp; Abandonment</h3>
                </div>
                <p>Abandonment plugs, squeeze cement volumes and balanced plug design.</p>
            </div>
            <div class="feature-card" data-page="Results">
                <div class="feature-head">
                    <div class="feature-icon">{icon("monitoring")}</div>
                    <h3>Results Dashboard</h3>
                </div>
                <p>Consolidated summary, PDF report export and cementing job procedure sheets.</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Cards are plain divs (not links) — wire each one to click its matching
    # sidebar radio option so it navigates to the page on click.
    bind_feature_cards()

    st.markdown(
        """
        <div class="home-callout">
            <strong>Getting started:</strong> Click a card above or pick a module from the
            sidebar to begin. Results are saved automatically and can be exported from
            the Results page.
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
