import pandas as pd
import streamlit as st


def inject_global_css():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

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
            font-size: 1.5rem;
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
            font-size: 1.2rem;
            margin-bottom: 0.75rem;
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
        }
        .stDownloadButton > button {
            background: #059669 !important;
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
            font-size: 1rem;
            flex-shrink: 0;
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


def page_header(icon: str, title: str, subtitle: str):
    st.markdown(
        f"""
        <div class="page-hero">
            <h1>{icon} {title}</h1>
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


def progress_overview(completed: int, total: int, modules: list):
    """render progress bar with module status chips"""
    pct = int((completed / total) * 100) if total else 0
    chips_html = ""
    for name, done in modules:
        cls = "done" if done else "pending"
        icon = "✓" if done else "○"
        chips_html += f'<span class="module-chip {cls}">{icon} {name}</span>'

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
