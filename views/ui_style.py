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
            max-width: 1180px;
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
            padding-top: 1.25rem;
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
            border-radius: 14px;
            padding: 2.5rem 3rem;
            margin-bottom: 1.5rem;
        }
        .home-hero h1 {
            font-size: 2rem;
            font-weight: 700;
            color: #FFFFFF !important;
            margin: 0 0 0.5rem 0;
        }
        .home-hero h1 .material-symbols-outlined {
            font-size: 2rem;
            color: #C9A227;
            vertical-align: -6px;
            margin-right: 0.4rem;
        }
        .home-hero .hero-sub {
            font-size: 0.95rem;
            color: #94A3B8 !important;
            margin: 0 0 1rem 0;
            max-width: 540px;
            line-height: 1.5;
        }
        .home-hero .hero-badges {
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        .hero-badge {
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 20px;
            padding: 0.3rem 0.85rem;
            font-size: 0.72rem;
            font-weight: 600;
            color: #E2E8F0;
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

        /* bordered panels */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0 !important;
            border-radius: 10px !important;
            box-shadow: 0 1px 4px rgba(15,23,42,0.04);
            padding: 0.25rem;
        }

        /* feature cards (home) */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
            margin: 1.25rem 0 0.5rem 0;
        }
        @media (max-width: 900px) {
            .feature-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 560px) {
            .feature-grid { grid-template-columns: 1fr; }
        }
        .feature-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 10px;
            padding: 1.25rem;
            box-shadow: 0 1px 4px rgba(0,0,0,0.03);
        }
        .feature-icon {
            width: 40px;
            height: 40px;
            background: #EEF2F7;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 0.75rem;
        }
        .feature-icon .material-symbols-outlined {
            font-size: 22px;
            color: #1565A8;
        }
        .feature-card h3 {
            font-size: 0.9rem;
            font-weight: 600;
            color: #0A2540;
            margin: 0 0 0.35rem 0;
        }
        .feature-card p {
            font-size: 0.78rem;
            color: #64748B;
            margin: 0;
            line-height: 1.5;
        }

        /* metrics */
        [data-testid="stMetric"] {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 0.75rem 1rem;
        }
        [data-testid="stMetricLabel"] {
            font-size: 0.75rem !important;
            color: #64748B !important;
            font-weight: 600 !important;
            text-transform: uppercase;
        }
        [data-testid="stMetricValue"] {
            font-size: 1.3rem !important;
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
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            overflow: hidden;
        }

        /* progress bar */
        .progress-card {
            background: #FFFFFF;
            border: 1px solid #E2E8F0;
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
            border: 1px solid #E2E8F0;
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
            border: 1px solid #E2E8F0;
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
    parent app page (scrolling, closing the sidebar, etc.)."""
    components.html(
        f"""
        <html><body style='margin:0;padding:0;overflow:hidden;'>
        {script}
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

    Runs a script inside a same-origin iframe that clicks Streamlit's
    native sidebar collapse button (stSidebarCollapseButton). Clicking
    this button triggers Streamlit's own collapse state, which keeps
    the expand/hamburger button (stExpandSidebarButton) visible.
    """
    _run_script(
        """
        <script>
        (function () {
            // Click the real <button> inside Streamlit's sidebar collapse
            // wrapper. The wrapper div (stSidebarCollapseButton) has no
            // handler of its own; only the inner button toggles the sidebar,
            // which makes Streamlit show the hamburger expand button too.
            function findAndClick() {
                var doc = window.parent.document;
                var wrapper = doc.querySelector('[data-testid="stSidebarCollapseButton"]');
                if (wrapper) {
                    var btn = wrapper.querySelector('button') || wrapper;
                    btn.click();
                    return true;
                }
                var selectors = [
                    'button[data-testid="stSidebarCollapseButton"]',
                    'button[data-testid="collapsedControl"]',
                    'section[data-testid="stSidebar"] button:first-child'
                ];
                for (var i = 0; i < selectors.length; i++) {
                    var btn = doc.querySelector(selectors[i]);
                    if (btn) {
                        btn.click();
                        return true;
                    }
                }
                return false;
            }
            if (findAndClick()) return;
            // Retry a few times in case the sidebar is still rendering
            var tries = 0;
            var timer = setInterval(function () {
                tries += 1;
                if (findAndClick() || tries > 30) clearInterval(timer);
            }, 100);
        })();
        </script>
        """
    )


def calculated_button(default_label: str, state_key: str, key: str):
    """Render a Calculate button that turns green and reads 'Calculated'
    once results are stored in session state, so the user gets durable
    confirmation that the calculation ran."""
    done = state_key in st.session_state
    return st.button(
        "Calculated" if done else default_label,
        width="stretch",
        type="primary" if done else "secondary",
        key=key,
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
