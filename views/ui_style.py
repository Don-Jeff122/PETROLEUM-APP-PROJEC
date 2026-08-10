import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


def inject_global_css():
    st.markdown(
        """
        <style>
        /* Fonts are served locally from the app's static/ folder so the UI
           looks identical even when Google Fonts is unreachable. */
        @font-face {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 400;
            font-display: swap;
            src: url('/app/static/Inter-400.woff2') format('woff2');
        }
        @font-face {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 500;
            font-display: swap;
            src: url('/app/static/Inter-500.woff2') format('woff2');
        }
        @font-face {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 600;
            font-display: swap;
            src: url('/app/static/Inter-600.woff2') format('woff2');
        }
        @font-face {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 700;
            font-display: swap;
            src: url('/app/static/Inter-700.woff2') format('woff2');
        }

        /* Material Symbols icon font — served locally so icons (ligatures)
           render as glyphs instead of literal words. */
        @font-face {
            font-family: "Material Symbols Outlined";
            font-style: normal;
            font-weight: 100 700;
            font-display: block;
            src: url('/app/static/MaterialSymbolsOutlined.woff2') format('woff2');
        }

        html, body, [class*="css"] {
            font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
        }

        /* app background */
        .stApp {
            background: #EEF2F7;
        }

        .block-container {
            padding-top: 1.25rem;
            padding-bottom: 2.5rem;
            max-width: 1500px;
        }

        /* sidebar */
        [data-testid="stSidebar"] {
            background: #071525;
        }

        /* sidebar expand toggle -> hamburger (three bars) */
        [data-testid="stExpandSidebarButton"] svg,
        [data-testid="stExpandSidebarButton"] span {
            display: none !important;
        }
        [data-testid="stExpandSidebarButton"]::before {
            content: "menu";
            font-family: 'Material Symbols Outlined';
            font-size: 24px;
            font-feature-settings: 'liga';
            line-height: 1;
            display: inline-block;
            color: #475569;
            transition: color 0.2s ease, transform 0.15s ease;
        }
        [data-testid="stExpandSidebarButton"]:hover::before {
            color: #0A2540;
        }
        [data-testid="stExpandSidebarButton"]:active::before {
            transform: scale(0.9);
        }
        [data-testid="stSidebar"] > div:first-child {
            padding-top: 0.5rem;
        }
        [data-testid="stSidebar"] * {
            color: #CBD5E1;
        }
        [data-testid="stSidebar"] .nav-section-label {
            font-size: 0.62rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #64748B !important;
            margin: 0.5rem 0 0.65rem 0.15rem;
        }
        [data-testid="stSidebar"] .stRadio label {
            padding: 0.5rem 0.85rem;
            margin-bottom: 3px;
            font-size: 0.84rem !important;
            font-weight: 500 !important;
        }
        [data-testid="stSidebar"] .stRadio label:has(input:checked) {
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }
        [data-testid="stSidebar"] hr {
            border: none;
            border-top: 1px solid rgba(255,255,255,0.08);
            margin: 0.75rem 0;
        }
        .sidebar-brand .app-name {
            font-size: 0.92rem;
            font-weight: 800;
            color: #FFFFFF !important;
            line-height: 1.2;
        }
        .sidebar-brand .app-tagline {
            font-size: 0.64rem;
            color: #64748B !important;
            margin-top: 0.2rem;
            line-height: 1.35;
            font-weight: 500;
        }
        .logo-fallback {
            width: 52px;
            height: 52px;
            background: #1565A8;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .logo-fallback .material-symbols-outlined {
            font-size: 28px;
            color: #FFFFFF;
        }
        .sidebar-footer {
            text-align: center;
            padding-top: 1rem;
            margin-top: 0.5rem;
            border-top: 1px solid rgba(255,255,255,0.08);
        }
        .sidebar-footer .version {
            font-size: 0.68rem;
            color: #475569 !important;
            font-weight: 600;
        }
        .sidebar-footer .author {
            font-size: 0.72rem;
            color: #64748B !important;
            margin-top: 0.2rem;
        }

        /* material symbols (icon font) */
        .material-symbols-outlined {
            font-family: 'Material Symbols Outlined';
            font-weight: normal;
            font-style: normal;
            font-size: 24px;
            line-height: 1;
            letter-spacing: normal;
            text-transform: none;
            display: inline-block;
            white-space: nowrap;
            word-wrap: normal;
            direction: ltr;
            -webkit-font-feature-settings: 'liga';
            font-feature-settings: 'liga';
            -webkit-font-smoothing: antialiased;
            vertical-align: middle;
        }

        /* page hero */
        .page-hero {
            background: #0A2540;
            border-radius: 12px;
            padding: 2rem 2.5rem;
            margin-bottom: 1.5rem;
            color: white;
        }
        .page-hero h1 {
            font-size: 1.8rem;
            font-weight: 700;
            margin: 0 0 0.35rem 0;
            color: white !important;
        }
        .page-hero h1 .material-symbols-outlined {
            font-size: 1.75rem;
            color: #C9A227;
            vertical-align: -5px;
            margin-right: 0.4rem;
        }
        .page-hero p {
            font-size: 0.92rem;
            opacity: 0.85;
            margin: 0;
            color: #CBD5E1 !important;
            max-width: 620px;
            line-height: 1.5;
        }

        /* home hero */
        .home-hero {
            background: #0A2540;
            border-radius: 12px;
            padding: 1.5rem 2rem;
            margin: 0.5rem 0 1.1rem 0;
        }
        .home-hero h1 {
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 1.55rem;
            font-weight: 700;
            letter-spacing: 0.01em;
            color: #FFFFFF !important;
            margin: 0 0 0.35rem 0;
        }
        .home-hero h1 .material-symbols-outlined {
            font-size: 1.55rem;
            color: #C9A227;
            vertical-align: -4px;
            margin-right: 0.4rem;
        }
        .home-hero .hero-sub {
            font-size: 0.84rem;
            color: #94A3B8 !important;
            margin: 0 0 0.8rem 0;
            max-width: 540px;
            line-height: 1.45;
        }
        .home-hero .hero-badges {
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
        }
        .hero-badge {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 0.22rem 0.7rem;
            font-size: 0.66rem;
            font-weight: 600;
            color: #E2E8F0;
        }

        /* home stats (text-only, sits directly on the page background) */
        .home-stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0.7rem;
            margin: 0 0 0.3rem 0;
        }
        @media (max-width: 700px) {
            .home-stats { grid-template-columns: 1fr; gap: 0.5rem; }
        }
        .home-stat {
            padding: 0.2rem 0;
        }
        .home-stat .hs-label {
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #64748B;
        }
        .home-stat .hs-value {
            font-size: 1.55rem;
            font-weight: 700;
            color: #0A2540;
            line-height: 1.15;
            margin-top: 0.15rem;
        }
        .home-stat .hs-delta {
            font-size: 0.78rem;
            color: #94A3B8;
            margin-top: 0.15rem;
        }

        /* section labels */
        .section-label {
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #C9A227;
            margin-bottom: 0.2rem;
        }
        .section-title {
            font-size: 1.05rem;
            font-weight: 700;
            color: #0A2540;
            margin: 0 0 0.85rem 0;
        }

        /* bordered panels: st.container(border=True) renders a
           FlexContainer with data-testid="stVerticalBlock" in this version,
           so target it directly to strip the outline (kept bg/radius). */
        [data-testid="stVerticalBlock"] {
            border: none !important;
        }

        /* widgets/panels that also draw outlines */
        [data-testid="stNumberInput"] [data-baseweb="input"],
        [data-testid="stNumberInput"] input,
        [data-testid="stTextInput"] [data-baseweb="input"],
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] [data-baseweb="textarea"],
        [data-testid="stTextArea"] textarea,
        [data-testid="stSelectbox"] [data-baseweb="select"],
        [data-testid="stMultiSelect"] [data-baseweb="select"],
        [data-testid="stDataFrame"],
        [data-testid="stDataEditor"],
        [data-testid="stTabs"] [data-baseweb="tab-list"],
        [data-testid="stExpander"] [data-testid="stExpanderDetails"],
        [data-testid="stPopover"] > div,
        [data-testid="stSlider"] [data-baseweb="slider"] {
            border: none !important;
            box-shadow: none !important;
            outline: none !important;
        }

        /* push the first card on every module down a little */
        [class*="st-key-module-first-card"] {
            margin-top: 0.5rem;
        }

        /* feature cards (home) */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 0.7rem;
            margin: 0.9rem 0 0.4rem 0;
        }
        @media (max-width: 1200px) {
            .feature-grid { grid-template-columns: repeat(3, 1fr); }
        }
        @media (max-width: 900px) {
            .feature-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 560px) {
            .feature-grid { grid-template-columns: 1fr; }
        }
        .feature-card {
            background: #FFFFFF;
            border: none;
            border-radius: 10px;
            padding: 0.8rem 0.9rem;
            box-shadow: 0 1px 4px rgba(0,0,0,0.03);
            cursor: pointer;
            transition: box-shadow 0.2s ease, transform 0.15s ease;
        }
        .feature-card:hover {
            box-shadow: 0 0 0 1px #C9A227, 0 4px 14px rgba(10, 37, 64, 0.12);
            transform: translateY(-2px);
        }
        .feature-head {
            display: flex;
            align-items: center;
            gap: 0.6rem;
            margin-bottom: 0.4rem;
        }
        .feature-icon {
            width: 32px;
            height: 32px;
            background: #EEF2F7;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .feature-icon .material-symbols-outlined {
            font-size: 19px;
            color: #1565A8;
        }
        .feature-card h3 {
            font-family: Georgia, 'Times New Roman', serif;
            font-size: 0.95rem;
            font-weight: 700;
            color: #0A2540;
            margin: 0;
        }
        .feature-card p {
            font-size: 0.74rem;
            color: #64748B;
            margin: 0;
            line-height: 1.45;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }

        /* metrics */
        [data-testid="stMetric"] {
            background: #FFFFFF;
            border: none;
            border-radius: 8px;
            padding: 0.5rem 0.9rem;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.7rem !important;
            color: #64748B !important;
            font-weight: 600 !important;
            text-transform: uppercase;
        }
        [data-testid="stMetricValue"] {
            font-size: 1.15rem !important;
            color: #0A2540 !important;
            font-weight: 700 !important;
        }

        /* inputs */
        [data-testid="stNumberInput"] label,
        [data-testid="stSelectbox"] label {
            font-weight: 600 !important;
            font-size: 0.82rem !important;
            color: #0F172A !important;
        }

        /* buttons */
        .stButton > button {
            background: #0A2540 !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            padding: 0.55rem 1.5rem !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
            transition: background-color 0.2s ease, transform 0.1s ease, box-shadow 0.2s ease;
        }
        .stButton > button:hover:not(:disabled) {
            background: #1565A8 !important;
            box-shadow: 0 2px 10px rgba(10, 37, 64, 0.25);
        }
        .stButton > button:active:not(:disabled) {
            background: #1E4E7F !important;
            transform: scale(0.97);
        }
        .stButton > button:focus {
            background: #1565A8 !important;
            box-shadow: 0 0 0 3px rgba(21, 101, 168, 0.35);
        }
        .stButton > button:focus-visible {
            outline: 2px solid #C9A227;
            outline-offset: 2px;
        }

        /* calculated buttons turn green to confirm the click worked */
        .stButton button[kind="primary"],
        .stButton button[data-testid="stBaseButton-primary"] {
            background: #059669 !important;
            color: white !important;
        }
        .stButton button[kind="primary"]:hover:not(:disabled),
        .stButton button[data-testid="stBaseButton-primary"]:hover:not(:disabled) {
            background: #047857 !important;
            box-shadow: 0 2px 10px rgba(5, 150, 105, 0.35);
        }
        .stButton button[kind="primary"]:active:not(:disabled),
        .stButton button[data-testid="stBaseButton-primary"]:active:not(:disabled) {
            background: #065F46 !important;
            transform: scale(0.97);
        }
        .stButton button[kind="primary"]:focus,
        .stButton button[data-testid="stBaseButton-primary"]:focus {
            background: #047857 !important;
            box-shadow: 0 0 0 3px rgba(5, 150, 105, 0.35);
        }

        /* clear buttons are outlined-red so they read as a destructive
           action, distinct from the dark Calculate buttons. The st-key-
           class is added by Streamlit from the button key. */
        .stButton button[class*="st-key-clear"] {
            background: #FFFFFF !important;
            color: #B91C1C !important;
            border: 1px solid #FECACA !important;
            font-weight: 600 !important;
        }
        .stButton button[class*="st-key-clear"]:hover:not(:disabled) {
            background: #FEF2F2 !important;
            color: #991B1B !important;
            border-color: #FCA5A5 !important;
            box-shadow: 0 2px 10px rgba(185, 28, 28, 0.18);
        }
        .stButton button[class*="st-key-clear"]:active:not(:disabled) {
            background: #FEE2E2 !important;
            transform: scale(0.97);
        }

        .stDownloadButton > button {
            background: #059669 !important;
            transition: background-color 0.2s ease, transform 0.1s ease;
        }
        .stDownloadButton > button:hover:not(:disabled) {
            background: #047857 !important;
        }
        .stDownloadButton > button:active:not(:disabled) {
            background: #065F46 !important;
            transform: scale(0.97);
        }

        /* alerts */
        [data-testid="stAlert"] {
            border-radius: 8px !important;
            border-left-width: 4px !important;
            font-size: 0.88rem;
        }

        /* dividers */
        hr {
            border: none;
            border-top: 1px solid #E2E8F0;
            margin: 1.5rem 0;
        }

        /* data tables */
        [data-testid="stDataFrame"] {
            border: none;
            border-radius: 8px;
            overflow: hidden;
        }

        /* progress bar */
        .progress-card {
            background: #FFFFFF;
            border: none;
            border-radius: 10px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.25rem;
        }
        .progress-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
        }
        .progress-header span {
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            color: #64748B;
        }
        .progress-header strong {
            font-size: 1.1rem;
            font-weight: 700;
            color: #0A2540;
        }
        .progress-track {
            height: 8px;
            background: #E2E8F0;
            border-radius: 999px;
            overflow: hidden;
        }
        .progress-fill {
            height: 100%;
            background: #1565A8;
            transition: width 0.6s ease;
        }
        .module-chips {
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
            margin-top: 0.75rem;
        }
        .module-chip {
            font-size: 0.68rem;
            font-weight: 600;
            padding: 0.25rem 0.6rem;
            border-radius: 999px;
        }
        .module-chip .chip-icon {
            font-size: 0.8rem;
            vertical-align: -2px;
            margin-right: 2px;
        }
        .module-chip.done {
            background: rgba(5,150,105,0.1);
            color: #059669;
        }
        .module-chip.pending {
            background: #F1F5F9;
            color: #64748B;
        }

        /* about page */
        .module-list {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        .module-item {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.6rem 0.85rem;
            background: #F8FAFC;
            border: none;
            border-radius: 8px;
        }
        .module-item .mi-icon {
            width: 32px;
            height: 32px;
            background: #EEF2F7;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .module-item .mi-icon .material-symbols-outlined {
            font-size: 19px;
            color: #1565A8;
        }
        .module-item .mi-name {
            font-size: 0.85rem;
            font-weight: 600;
            color: #0A2540;
        }
        .dev-card {
            background: #0A2540;
            border-radius: 10px;
            padding: 1.25rem 1.5rem;
            color: white;
            margin-top: 0.5rem;
        }
        .dev-card .dev-label {
            font-size: 0.65rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: #C9A227;
            margin-bottom: 0.5rem;
        }
        .dev-card .dev-name {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.35rem;
        }
        .dev-card .dev-detail {
            font-size: 0.78rem;
            color: #94A3B8;
            line-height: 1.5;
        }

        /* home callout */
        .home-callout {
            background: #F8FAFC;
            border-left: 4px solid #C9A227;
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-top: 0.5rem;
            font-size: 0.88rem;
            color: #0F172A;
            line-height: 1.5;
        }

        /* hide streamlit chrome */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header[data-testid="stHeader"] {
            background: transparent;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def icon(name: str, cls: str = ""):
    """Return Material Symbols icon markup (font-based, no emoji).

    ``name`` is the snake_case icon name, e.g. ``"oil_barrel"``.
    """
    return f'<span class="material-symbols-outlined {cls}">{name}</span>'


def page_header(icon_name: str, title: str, subtitle: str):
    st.markdown(
        f"""
        <div class="page-hero">
            <h1>{icon(icon_name)} {title}</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_title(label: str, title: str):
    st.markdown(
        f'<div class="section-label">{label}</div>'
        f'<div class="section-title">{title}</div>',
        unsafe_allow_html=True,
    )


def _run_script(script: str):
    """Embed a script inside a hidden same-origin iframe so it can drive the
    parent app page (scrolling, closing the sidebar, etc.).

    A unique nonce is embedded in the iframe's srcdoc on every call. Without
    it, Streamlit keeps the iframe's srcDoc unchanged across reruns, the
    iframe is not reloaded, and the embedded script only executes once per
    page load (e.g. the sidebar only auto-collapses on the first navigation).
    """
    import time

    nonce = f"{time.time_ns()}"
    components.html(
        f"""
        <html><body style='margin:0;padding:0;overflow:hidden;'>
        {script}
        <!-- nonce:{nonce} -->
        </body></html>
        """,
        height=1,
        width=1,
    )


def results_anchor():
    """Render an invisible anchor that the browser scrolls to after a
    calculation button is clicked (results live below the input form).
    Must be called before scroll_to_results()."""
    st.markdown('<div id="results-anchor"></div>', unsafe_allow_html=True)


def scroll_to_results():
    """Smooth-scroll the page down to the results after a calculate click.

    The script runs inside an iframe that Streamlit grants JavaScript
    execution and same-origin access to the app, so it can reach the parent
    document. It retries briefly to cover Streamlit's streaming render order.
    """
    _run_script(
        """
        <script>
        (function () {
            var doc = window.parent.document;
            var tries = 0;
            function findAndScroll() {
                var el = doc.getElementById("results-anchor");
                if (!el) return false;
                el.scrollIntoView({ behavior: "smooth", block: "start" });
                return true;
            }
            if (findAndScroll()) return;
            var timer = setInterval(function () {
                tries += 1;
                if (findAndScroll() || tries > 25) clearInterval(timer);
            }, 120);
        })();
        </script>
        """
    )


def close_sidebar():
    """Collapse the sidebar automatically after the user picks a page,
    so the module content is fully visible.

    Runs a script inside a same-origin iframe that first checks Streamlit's
    own sidebar state via the ``aria-expanded`` attribute on the sidebar
    root. If the sidebar is already collapsed it does nothing (this prevents
    a stray click from re-opening it, which matters on mobile where the
    drawer may already close on selection). Otherwise it clicks the native
    collapse button (stSidebarCollapseButton) — or falls back to the header
    hamburger toggle — and keeps polling until the sidebar reports closed.
    """
    _run_script(
        """
        <script>
        (function () {
            var doc = window.parent.document;
            var tries = 0;
            var clickedOnce = false;
            // The sidebar root exposes aria-expanded=false when it is
            // collapsed (desktop rail or hidden mobile drawer).
            function sidebarOpen() {
                var sb = doc.querySelector('[data-testid="stSidebar"]');
                if (!sb) return null;
                return sb.getAttribute('aria-expanded') !== 'false';
            }
            function clickCollapse() {
                var wrapper = doc.querySelector('[data-testid="stSidebarCollapseButton"]');
                if (wrapper) {
                    var btn = wrapper.querySelector('button') || wrapper;
                    btn.click();
                    return true;
                }
                var toggle = doc.querySelector('button[data-testid="stExpandSidebarButton"]');
                if (toggle) {
                    toggle.click();
                    return true;
                }
                return false;
            }
            function attempt() {
                var open = sidebarOpen();
                if (open === null) return false; // sidebar not rendered yet
                if (open === false) return true; // already collapsed - done
                if (!clickedOnce) {
                    clickedOnce = true;
                    clickCollapse();
                }
                return false; // keep polling until aria-expanded flips
            }
            if (attempt()) return;
            var timer = setInterval(function () {
                tries += 1;
                if (attempt() || tries > 30) clearInterval(timer);
            }, 120);
        })();
        </script>
        """
    )


def bind_feature_cards():
    """Make the Home feature cards navigate to their module pages on click.

    The cards are plain divs (not links), each carrying a ``data-page``
    attribute that matches a sidebar radio option. This script (inside a
    hidden same-origin iframe, same mechanism as ``close_sidebar``) simulates
    a click on that radio option so Streamlit itself performs the navigation
    — no URL change and no full page reload.
    """
    _run_script(
        """
        <script>
        (function () {
            var doc = window.parent.document;
            var tries = 0;
            function bind() {
                var cards = doc.querySelectorAll('.feature-card[data-page]');
                if (!cards.length) return false;
                for (var i = 0; i < cards.length; i++) {
                    (function (card) {
                        if (card.dataset.bound) return;
                        card.dataset.bound = '1';
                        card.addEventListener('click', function () {
                            var target = (card.getAttribute('data-page') || '').trim();
                            // textContent (not innerText) so matching still works
                            // when the sidebar is collapsed/hidden.
                            var options = doc.querySelectorAll(
                                '[data-testid="stSidebar"] label[data-testid="stRadioOption"]'
                            );
                            for (var j = 0; j < options.length; j++) {
                                var text = (options[j].textContent || '')
                                    .replace(/\\s+/g, ' ').trim();
                                if (text === target) {
                                    var input = options[j].querySelector('input[type="radio"]');
                                    if (input) { input.click(); } else { options[j].click(); }
                                    return;
                                }
                            }
                            console.warn('[feature-card] no sidebar option for:', target);
                        });
                    })(cards[i]);
                }
                return true;
            }
            if (bind()) return;
            var timer = setInterval(function () {
                tries += 1;
                if (bind() || tries > 25) clearInterval(timer);
            }, 100);
        })();
        </script>
        """
    )


def calculated_button(default_label: str, state_key: str, key: str, inputs=None):
    """Render a Calculate button that turns green and reads 'Calculated'
    after a successful calculation, and flips back to 'Calculate' whenever
    any input changes.

    ``done`` is true when results exist in session state AND the current
    inputs still match the snapshot saved with those results. On the very
    run where the button is clicked, the results are only saved later in
    that run, so the click state (already present in session state before
    the widget is instantiated) is used instead to show the green
    'Calculated' state immediately.
    """
    clicked_this_run = bool(st.session_state.get(key, False))
    done = state_key in st.session_state
    if done and inputs is not None:
        done = st.session_state.get(f"{state_key}_inputs") == inputs
    done = done or clicked_this_run
    return st.button(
        "Calculated" if done else default_label,
        width="stretch",
        type="primary" if done else "secondary",
        key=key,
    )


def save_calculation(state_key: str, results: dict, inputs=None):
    """Store calculation results together with a snapshot of the inputs that
    produced them. ``calculated_button`` compares the current inputs against
    this snapshot to detect stale results."""
    st.session_state[state_key] = results
    if inputs is not None:
        st.session_state[f"{state_key}_inputs"] = dict(inputs)


def _clear_saved_results(state_key: str):
    """Delete a module's saved results and input snapshot from session state."""
    for key in (state_key, f"{state_key}_inputs"):
        if key in st.session_state:
            del st.session_state[key]


def results_current(state_key: str, inputs=None) -> bool:
    """True when saved results exist and (if ``inputs`` is given) they were
    computed from exactly the current inputs. Used to re-render a module's
    results when the user returns to it without re-running the calculation."""
    if state_key not in st.session_state:
        return False
    if inputs is None:
        return True
    return st.session_state.get(f"{state_key}_inputs") == inputs


def clear_results_button(state_key: str, label: str = "Clear Results"):
    """Render a red 'Clear' button at the bottom-right of a module's results.

    Clicking it removes the saved results (and their input snapshot) from
    session state so the calculation no longer lingers on the site. The
    deletion runs in an ``on_click`` callback, which fires before the script
    body re-runs — important because the results (and this button) are only
    rendered inside the ``if calculate:`` block.
    """
    _, right = st.columns([4, 1], vertical_alignment="bottom")
    with right:
        st.button(
            label,
            key=f"clear_{state_key}",
            width="stretch",
            on_click=_clear_saved_results,
            args=(state_key,),
        )


def begin_calculation(message: str):
    """Give immediate feedback that a Calculate button was clicked: show a
    toast and scroll the page down to the results rendered below the form.
    Call this as the first statement of an ``if calculate:`` block."""
    st.toast(message)
    results_anchor()
    scroll_to_results()


def progress_overview(completed: int, total: int, modules: list):
    """render progress bar with module status chips"""
    pct = int((completed / total) * 100) if total else 0
    chips_html = ""
    for name, done in modules:
        cls = "done" if done else "pending"
        mark = icon("check_circle", "chip-icon") if done else icon(
            "radio_button_unchecked", "chip-icon"
        )
        chips_html += f'<span class="module-chip {cls}">{mark} {name}</span>'

    st.markdown(
        f"""
        <div class="progress-card">
            <div class="progress-header">
                <span>Workflow Progress</span>
                <strong>{completed} / {total} modules</strong>
            </div>
            <div class="progress-track">
                <div class="progress-fill" style="width: {pct}%;"></div>
            </div>
            <div class="module-chips">{chips_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def results_table(parameters: list, values: list):
    df = pd.DataFrame({"Parameter": parameters, "Value": values})
    st.dataframe(df, width="stretch", hide_index=True)


def apply_plotly_style(fig):
    fig.update_layout(
        template="plotly_white",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={"family": "Inter, Segoe UI, sans-serif", "color": "#0F172A"},
        title={"font": {"size": 16, "color": "#0A2540"}},
        height=460,
        margin={"l": 48, "r": 24, "t": 56, "b": 48},
    )
    fig.update_xaxes(gridcolor="#E2E8F0", linecolor="#CBD5E1")
    fig.update_yaxes(gridcolor="#E2E8F0", linecolor="#CBD5E1")
    return fig
