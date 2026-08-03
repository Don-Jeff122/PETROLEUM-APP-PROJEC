import pandas as pd
import streamlit as st

# Brand palette — deep petroleum navy with gold accent
COLORS = {
    "primary": "#0A2540",
    "secondary": "#1565A8",
    "accent": "#C9A227",
    "accent_light": "#E8C547",
    "bg": "#EEF2F7",
    "bg_subtle": "#F8FAFC",
    "card": "#FFFFFF",
    "text": "#0F172A",
    "muted": "#64748B",
    "border": "#E2E8F0",
    "success": "#059669",
    "warning": "#D97706",
    "danger": "#DC2626",
    "sidebar": "#071525",
    "sidebar_mid": "#0F2744",
}

PLOTLY_LAYOUT = {
    "template": "plotly_white",
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(0,0,0,0)",
    "font": {"family": "Inter, Segoe UI, sans-serif", "color": COLORS["text"]},
    "title": {"font": {"size": 16, "color": COLORS["primary"]}},
    "height": 460,
    "margin": {"l": 48, "r": 24, "t": 56, "b": 48},
    "legend": {"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "right", "x": 1},
    "colorway": [COLORS["secondary"], COLORS["accent"], COLORS["success"], COLORS["danger"]],
}


def inject_global_css():
    c = COLORS
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        :root {{
            --pm-primary: {c["primary"]};
            --pm-secondary: {c["secondary"]};
            --pm-accent: {c["accent"]};
            --pm-bg: {c["bg"]};
            --pm-card: {c["card"]};
            --pm-text: {c["text"]};
            --pm-muted: {c["muted"]};
            --pm-border: {c["border"]};
        }}

        html, body, [class*="css"] {{
            font-family: 'Inter', 'Segoe UI', system-ui, sans-serif;
        }}

        /* ── App background ── */
        .stApp {{
            background:
                radial-gradient(ellipse 80% 50% at 50% -10%, rgba(21,101,168,0.08) 0%, transparent 60%),
                linear-gradient(180deg, {c["bg"]} 0%, #E4EAF2 100%);
        }}

        .block-container {{
            padding-top: 1.25rem;
            padding-bottom: 2.5rem;
            max-width: 1180px;
        }}

        /* ── Sidebar ── */
        [data-testid="stSidebar"] {{
            background: linear-gradient(175deg, {c["sidebar"]} 0%, {c["sidebar_mid"]} 55%, #132D4A 100%);
            border-right: 1px solid rgba(255,255,255,0.06);
        }}
        [data-testid="stSidebar"] > div:first-child {{
            padding-top: 1.25rem;
        }}
        [data-testid="stSidebar"] * {{
            color: #CBD5E1;
        }}
        [data-testid="stSidebar"] .nav-section-label {{
            font-size: 0.62rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #64748B !important;
            margin: 0.5rem 0 0.65rem 0.15rem;
        }}
        [data-testid="stSidebar"] .stRadio label {{
            background: rgba(255,255,255,0.04);
            border: 1px solid rgba(255,255,255,0.07);
            border-radius: 10px;
            padding: 0.5rem 0.85rem;
            margin-bottom: 3px;
            transition: all 0.18s ease;
            cursor: pointer;
            font-size: 0.84rem !important;
            font-weight: 500 !important;
        }}
        [data-testid="stSidebar"] .stRadio label:hover {{
            background: rgba(255,255,255,0.1);
            border-color: rgba(201,162,39,0.45);
            transform: translateX(2px);
        }}
        [data-testid="stSidebar"] .stRadio label:has(input:checked) {{
            background: linear-gradient(135deg, rgba(21,101,168,0.35), rgba(201,162,39,0.18));
            border-color: {c["accent"]};
            color: #FFFFFF !important;
            font-weight: 600 !important;
            box-shadow: 0 2px 12px rgba(201,162,39,0.15);
        }}
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {{
            gap: 3px;
        }}
        [data-testid="stSidebar"] hr {{
            border: none;
            border-top: 1px solid rgba(255,255,255,0.08);
            margin: 0.75rem 0;
        }}
        .sidebar-brand .app-name {{
            font-size: 0.92rem;
            font-weight: 800;
            color: #FFFFFF !important;
            letter-spacing: -0.02em;
            line-height: 1.2;
        }}
        .sidebar-brand .app-tagline {{
            font-size: 0.64rem;
            color: #64748B !important;
            margin-top: 0.2rem;
            line-height: 1.35;
            font-weight: 500;
        }}
        .logo-fallback {{
            width: 52px;
            height: 52px;
            background: linear-gradient(135deg, {c["secondary"]}, {c["accent"]});
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        }}
        .sidebar-footer {{
            text-align: center;
            padding-top: 1rem;
            margin-top: 0.5rem;
            border-top: 1px solid rgba(255,255,255,0.08);
        }}
        .sidebar-footer .version {{
            font-size: 0.68rem;
            color: #475569 !important;
            font-weight: 600;
            letter-spacing: 0.04em;
        }}
        .sidebar-footer .author {{
            font-size: 0.72rem;
            color: #64748B !important;
            margin-top: 0.2rem;
        }}

        /* ── Page hero ── */
        .page-hero {{
            background: linear-gradient(125deg, {c["primary"]} 0%, {c["secondary"]} 55%, #1a7fd4 100%);
            border-radius: 18px;
            padding: 2rem 2.5rem;
            margin-bottom: 1.5rem;
            color: white;
            position: relative;
            overflow: hidden;
            box-shadow:
                0 1px 0 rgba(255,255,255,0.1) inset,
                0 12px 40px rgba(10,37,64,0.28);
        }}
        .page-hero::before {{
            content: '';
            position: absolute;
            top: -40%;
            right: -8%;
            width: 280px;
            height: 280px;
            background: radial-gradient(circle, rgba(201,162,39,0.18) 0%, transparent 70%);
            pointer-events: none;
        }}
        .page-hero::after {{
            content: '';
            position: absolute;
            bottom: -30%;
            left: 20%;
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(255,255,255,0.06) 0%, transparent 70%);
            pointer-events: none;
        }}
        .page-hero h1 {{
            font-size: 1.8rem;
            font-weight: 800;
            margin: 0 0 0.35rem 0;
            color: white !important;
            letter-spacing: -0.03em;
            position: relative;
            z-index: 1;
        }}
        .page-hero p {{
            font-size: 0.92rem;
            opacity: 0.9;
            margin: 0;
            color: #CBD5E1 !important;
            position: relative;
            z-index: 1;
            max-width: 620px;
            line-height: 1.5;
        }}

        /* ── Home hero (larger) ── */
        .home-hero {{
            background: linear-gradient(125deg, {c["primary"]} 0%, {c["secondary"]} 50%, #1976D2 100%);
            border-radius: 20px;
            padding: 2.75rem 3rem;
            margin-bottom: 1.75rem;
            position: relative;
            overflow: hidden;
            box-shadow: 0 16px 48px rgba(10,37,64,0.3);
        }}
        .home-hero::before {{
            content: '';
            position: absolute;
            inset: 0;
            background:
                radial-gradient(circle at 85% 20%, rgba(201,162,39,0.22) 0%, transparent 45%),
                radial-gradient(circle at 10% 80%, rgba(255,255,255,0.05) 0%, transparent 40%);
            pointer-events: none;
        }}
        .home-hero h1 {{
            font-size: 2.1rem;
            font-weight: 800;
            color: #FFFFFF !important;
            margin: 0 0 0.5rem 0;
            letter-spacing: -0.03em;
            position: relative;
        }}
        .home-hero .hero-sub {{
            font-size: 1rem;
            color: #94A3B8 !important;
            margin: 0 0 1.25rem 0;
            position: relative;
            max-width: 540px;
            line-height: 1.55;
        }}
        .home-hero .hero-badges {{
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
            position: relative;
        }}
        .hero-badge {{
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.15);
            border-radius: 999px;
            padding: 0.3rem 0.85rem;
            font-size: 0.72rem;
            font-weight: 600;
            color: #E2E8F0;
            letter-spacing: 0.02em;
        }}

        /* ── Section labels ── */
        .section-label {{
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: {c["accent"]};
            margin-bottom: 0.2rem;
        }}
        .section-title {{
            font-size: 1.05rem;
            font-weight: 700;
            color: {c["primary"]};
            margin: 0 0 0.85rem 0;
            letter-spacing: -0.01em;
        }}

        /* ── Bordered panels ── */
        [data-testid="stVerticalBlockBorderWrapper"] {{
            background: {c["card"]};
            border: 1px solid {c["border"]} !important;
            border-radius: 14px !important;
            box-shadow: 0 2px 12px rgba(15,23,42,0.04);
            padding: 0.25rem;
            transition: box-shadow 0.2s ease;
        }}
        [data-testid="stVerticalBlockBorderWrapper"]:hover {{
            box-shadow: 0 4px 20px rgba(15,23,42,0.07);
        }}

        /* ── Feature cards (home) ── */
        .feature-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1rem;
            margin: 1.25rem 0 0.5rem 0;
        }}
        @media (max-width: 900px) {{
            .feature-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}
        @media (max-width: 560px) {{
            .feature-grid {{ grid-template-columns: 1fr; }}
        }}
        .feature-card {{
            background: {c["card"]};
            border: 1px solid {c["border"]};
            border-radius: 14px;
            padding: 1.35rem 1.25rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease;
            position: relative;
            overflow: hidden;
        }}
        .feature-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: linear-gradient(90deg, {c["secondary"]}, {c["accent"]});
            opacity: 0;
            transition: opacity 0.22s ease;
        }}
        .feature-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 12px 32px rgba(10,37,64,0.12);
            border-color: {c["secondary"]};
        }}
        .feature-card:hover::before {{
            opacity: 1;
        }}
        .feature-icon {{
            width: 42px;
            height: 42px;
            background: linear-gradient(135deg, rgba(21,101,168,0.1), rgba(201,162,39,0.12));
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.3rem;
            margin-bottom: 0.75rem;
        }}
        .feature-card h3 {{
            font-size: 0.92rem;
            font-weight: 700;
            color: {c["primary"]};
            margin: 0 0 0.4rem 0;
        }}
        .feature-card p {{
            font-size: 0.78rem;
            color: {c["muted"]};
            margin: 0;
            line-height: 1.5;
        }}

        /* ── Metrics ── */
        [data-testid="stMetric"] {{
            background: {c["card"]};
            border: 1px solid {c["border"]};
            border-radius: 12px;
            padding: 0.85rem 1.1rem;
            box-shadow: 0 1px 6px rgba(0,0,0,0.03);
            transition: border-color 0.2s ease;
        }}
        [data-testid="stMetric"]:hover {{
            border-color: {c["secondary"]};
        }}
        [data-testid="stMetricLabel"] {{
            font-size: 0.75rem !important;
            color: {c["muted"]} !important;
            font-weight: 600 !important;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}
        [data-testid="stMetricValue"] {{
            font-size: 1.4rem !important;
            color: {c["primary"]} !important;
            font-weight: 800 !important;
            letter-spacing: -0.02em;
        }}
        [data-testid="stMetricDelta"] {{
            font-size: 0.72rem !important;
        }}

        /* ── Inputs ── */
        [data-testid="stNumberInput"] input,
        [data-testid="stSelectbox"] div[data-baseweb="select"] {{
            border-radius: 8px !important;
        }}
        [data-testid="stNumberInput"] label,
        [data-testid="stSelectbox"] label {{
            font-weight: 600 !important;
            font-size: 0.82rem !important;
            color: {c["text"]} !important;
        }}

        /* ── Buttons ── */
        .stButton > button {{
            background: linear-gradient(135deg, {c["primary"]}, {c["secondary"]}) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.6rem 1.75rem !important;
            font-weight: 700 !important;
            font-size: 0.88rem !important;
            letter-spacing: 0.02em !important;
            box-shadow: 0 4px 16px rgba(10,37,64,0.28) !important;
            transition: all 0.2s ease !important;
        }}
        .stButton > button:hover {{
            box-shadow: 0 8px 24px rgba(10,37,64,0.38) !important;
            transform: translateY(-1px);
        }}
        .stButton > button:active {{
            transform: translateY(0);
        }}
        .stDownloadButton > button {{
            background: linear-gradient(135deg, {c["success"]}, #047857) !important;
            box-shadow: 0 4px 16px rgba(5,150,105,0.3) !important;
        }}

        /* ── Alerts ── */
        [data-testid="stAlert"] {{
            border-radius: 10px !important;
            border-left-width: 4px !important;
            font-size: 0.88rem;
        }}

        /* ── Dividers ── */
        hr {{
            border: none;
            border-top: 1px solid {c["border"]};
            margin: 1.5rem 0;
        }}

        /* ── Data tables ── */
        [data-testid="stDataFrame"] {{
            border: 1px solid {c["border"]};
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 1px 4px rgba(0,0,0,0.03);
        }}

        /* ── Progress bar (results) ── */
        .progress-card {{
            background: {c["card"]};
            border: 1px solid {c["border"]};
            border-radius: 14px;
            padding: 1.25rem 1.5rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 2px 12px rgba(15,23,42,0.04);
        }}
        .progress-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 0.75rem;
        }}
        .progress-header span {{
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: {c["muted"]};
        }}
        .progress-header strong {{
            font-size: 1.1rem;
            font-weight: 800;
            color: {c["primary"]};
        }}
        .progress-track {{
            height: 8px;
            background: {c["border"]};
            border-radius: 999px;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg, {c["secondary"]}, {c["accent"]});
            transition: width 0.6s ease;
        }}
        .module-chips {{
            display: flex;
            gap: 0.4rem;
            flex-wrap: wrap;
            margin-top: 0.75rem;
        }}
        .module-chip {{
            font-size: 0.68rem;
            font-weight: 600;
            padding: 0.25rem 0.6rem;
            border-radius: 999px;
            letter-spacing: 0.02em;
        }}
        .module-chip.done {{
            background: rgba(5,150,105,0.12);
            color: {c["success"]};
            border: 1px solid rgba(5,150,105,0.25);
        }}
        .module-chip.pending {{
            background: rgba(100,116,139,0.08);
            color: {c["muted"]};
            border: 1px solid {c["border"]};
        }}

        /* ── About page ── */
        .module-list {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}
        .module-item {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.65rem 0.85rem;
            background: {c["bg_subtle"]};
            border: 1px solid {c["border"]};
            border-radius: 10px;
            transition: background 0.18s ease;
        }}
        .module-item:hover {{
            background: rgba(21,101,168,0.06);
            border-color: {c["secondary"]};
        }}
        .module-item .mi-icon {{
            width: 32px;
            height: 32px;
            background: linear-gradient(135deg, rgba(21,101,168,0.12), rgba(201,162,39,0.1));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1rem;
            flex-shrink: 0;
        }}
        .module-item .mi-name {{
            font-size: 0.85rem;
            font-weight: 600;
            color: {c["primary"]};
        }}
        .dev-card {{
            background: linear-gradient(135deg, {c["primary"]}, {c["secondary"]});
            border-radius: 14px;
            padding: 1.25rem 1.5rem;
            color: white;
            margin-top: 0.5rem;
        }}
        .dev-card .dev-label {{
            font-size: 0.65rem;
            font-weight: 700;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            color: {c["accent_light"]};
            margin-bottom: 0.5rem;
        }}
        .dev-card .dev-name {{
            font-size: 1.1rem;
            font-weight: 800;
            margin-bottom: 0.35rem;
        }}
        .dev-card .dev-detail {{
            font-size: 0.78rem;
            color: #94A3B8;
            line-height: 1.5;
        }}

        /* ── Info callout (home) ── */
        .home-callout {{
            background: linear-gradient(135deg, rgba(21,101,168,0.06), rgba(201,162,39,0.05));
            border: 1px solid rgba(21,101,168,0.15);
            border-left: 4px solid {c["accent"]};
            border-radius: 12px;
            padding: 1rem 1.25rem;
            margin-top: 0.5rem;
            font-size: 0.88rem;
            color: {c["text"]};
            line-height: 1.55;
        }}

        /* ── Hide Streamlit chrome ── */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header[data-testid="stHeader"] {{
            background: transparent;
        }}
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
    """Render a styled progress bar with module status chips."""
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
    st.dataframe(df, use_container_width=True, hide_index=True)


def apply_plotly_style(fig):
    fig.update_layout(**PLOTLY_LAYOUT)
    fig.update_xaxes(gridcolor=COLORS["border"], linecolor="#CBD5E1", zerolinecolor="#CBD5E1")
    fig.update_yaxes(gridcolor=COLORS["border"], linecolor="#CBD5E1", zerolinecolor="#CBD5E1")
    return fig


def status_message(status: str, messages: dict):
    msg = messages.get(status, "")
    if not msg:
        return
    if status in ("SAFE", "GOOD"):
        st.success(msg)
    elif status in ("FAIR",):
        st.warning(msg)
    else:
        st.error(msg)
