from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from modules.constants import APP_NAME, APP_VERSION, AUTHOR

# ── Brand palette ────────────────────────────────────────────────────────────
PRIMARY = colors.HexColor("#0A2540")
SECONDARY = colors.HexColor("#1565A8")
ACCENT = colors.HexColor("#C9A227")
MUTED = colors.HexColor("#64748B")
BORDER = colors.HexColor("#E2E8F0")
ROW_ALT = colors.HexColor("#F8FAFC")
SUCCESS = colors.HexColor("#059669")


def _base_styles():
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        "JobTitle",
        parent=styles["Title"],
        fontSize=20,
        alignment=TA_CENTER,
        textColor=PRIMARY,
        spaceAfter=4,
    )
    subtitle_style = ParagraphStyle(
        "JobSubtitle",
        parent=styles["Normal"],
        fontSize=11,
        alignment=TA_CENTER,
        textColor=MUTED,
        spaceAfter=10,
    )
    heading_style = ParagraphStyle(
        "JobHeading",
        parent=styles["Heading2"],
        fontSize=13,
        textColor=SECONDARY,
        spaceBefore=14,
        spaceAfter=6,
    )
    body_style = ParagraphStyle(
        "JobBody",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        spaceAfter=6,
    )
    return title_style, subtitle_style, heading_style, body_style


def _table(data, col_widths, header_bg=PRIMARY, status_col=None):
    table = Table(data, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), header_bg),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, ROW_ALT]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
    ]
    if status_col is not None:
        for row in range(1, len(data)):
            if data[row][status_col] in ("OK", "PASS", "SAFE", "GOOD"):
                style.append(("TEXTCOLOR", (status_col, row), (status_col, row), SUCCESS))
                style.append(("FONTNAME", (status_col, row), (status_col, row), "Helvetica-Bold"))
    table.setStyle(TableStyle(style))
    return table


def generate_report(filename, sections):
    """Generic engineering calculation report from saved session results."""
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=22 * mm,
        leftMargin=22 * mm,
        topMargin=22 * mm,
        bottomMargin=22 * mm,
    )
    title_style, subtitle_style, _, _ = _base_styles()

    elements = []
    elements.append(Paragraph(f"<b>{APP_NAME}</b>", title_style))
    elements.append(Paragraph(
        f"Drilling Engineering Calculation Report — {datetime.now().strftime('%d %b %Y')}",
        subtitle_style,
    ))
    elements.append(HRFlowable(width="100%", thickness=1.5, color=SECONDARY, spaceAfter=12))

    for title, data in sections.items():
        elements.append(Paragraph(f"<b>{title}</b>", subtitle_style))
        table_data = [["Parameter", "Value"]]
        for key, value in data.items():
            if key == "Additives":
                continue
            if isinstance(value, float):
                table_data.append([key, f"{value:.4g}"])
            else:
                table_data.append([key, str(value)])
        elements.append(_table(table_data, [90 * mm, 85 * mm]))
        elements.append(Spacer(1, 10))

    doc.build(elements)


def generate_job_procedure(filename, cement):
    """Generate a formal Cementing Job Procedure Sheet (Milestone 2 deliverable)."""
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
    )
    title_style, subtitle_style, heading_style, body_style = _base_styles()

    elements = []
    elements.append(Paragraph("CEMENTING JOB PROCEDURE SHEET", title_style))
    elements.append(Paragraph(
        f"{APP_NAME} — {APP_VERSION} · Generated {datetime.now().strftime('%d %b %Y, %H:%M')}",
        subtitle_style,
    ))
    elements.append(HRFlowable(width="100%", thickness=2, color=ACCENT, spaceAfter=12))

    # ── Job identification ──
    elements.append(Paragraph("1. Job Identification", heading_style))
    well_data = [
        ["Well Name", "—", "Field / Block", "—"],
        ["Operator", "—", "Rig", "—"],
        ["Job Type", "Primary Cementing", "Cement Class", cement.get("Cement Class", "—")],
        ["Date", datetime.now().strftime("%d %b %Y"), "Prepared By", AUTHOR],
    ]
    elements.append(_table(well_data, [38 * mm, 48 * mm, 38 * mm, 48 * mm]))
    elements.append(Spacer(1, 6))

    # ── Slurry & temperature ──
    elements.append(Paragraph("2. Slurry Design & Temperature Rating", heading_style))
    temp_rating = cement.get("Temperature Rating", "OK")
    slurry_data = [
        ["Parameter", "Value", "Parameter", "Value"],
        ["Cement Density", f"{cement.get('Density (ppg)', 0):.2f} ppg",
         "Yield per Sack", f"{cement.get('Yield (m³/sack)', 0):.3f} m³/sack"],
        ["Class Max Temp", f"{cement.get('Max Temp (°C)', 0):.0f} °C",
         "Bottom-Hole Temp", f"{cement.get('Bottom-Hole Temp (°C)', 0):.0f} °C"],
        ["Temperature Rating", temp_rating, "Status", "PASS" if temp_rating == "OK" else "CHECK"],
    ]
    elements.append(_table(slurry_data, [42 * mm, 40 * mm, 42 * mm, 38 * mm], status_col=3))
    elements.append(Spacer(1, 6))

    # ── Volumetrics ──
    elements.append(Paragraph("3. Volumetrics & Pump Schedule", heading_style))
    vol_data = [
        ["Parameter", "Value", "Parameter", "Value"],
        ["Annular Slurry Volume", f"{cement.get('Slurry Volume', 0):.2f} m³",
         "Required Cement", f"{cement.get('Required Cement', 0):.0f} sacks"],
        ["Lead Slurry", f"{cement.get('Lead Volume', 0):.2f} m³",
         "Tail Slurry", f"{cement.get('Tail Volume', 0):.2f} m³"],
        ["Spacer Volume", f"{cement.get('Spacer Volume', 0):.2f} m³",
         "Flush Volume", f"{cement.get('Flush Volume', 0):.2f} m³"],
        ["Pump Time", f"{cement.get('Pump Time', 0):.1f} min",
         "Bumping Pressure", f"{cement.get('Bumping Pressure (Pa)', 0) / 1_000_000:.2f} MPa"],
    ]
    elements.append(_table(vol_data, [42 * mm, 40 * mm, 42 * mm, 38 * mm]))
    elements.append(Spacer(1, 6))

    # ── Additive schedule ──
    additives = cement.get("Additives", [])
    if additives:
        elements.append(Paragraph("4. Additive Schedule", heading_style))
        add_data = [["Additive", "Category", "Dosage (kg/sack)", "Total (kg)", "Conc. (kg/m³)", "Max Temp (°C)"]]
        for row in additives:
            add_data.append([
                row["Additive"],
                row["Category"],
                f"{row['Dosage (kg/sack)']:.2f}",
                f"{row['Total (kg)']:.1f}",
                f"{row['Concentration (kg/m³)']:.1f}",
                f"{row['Max Temp (°C)']:.0f}",
            ])
        elements.append(_table(add_data, [32 * mm, 30 * mm, 32 * mm, 24 * mm, 28 * mm, 22 * mm]))

    # ── Sign-off ──
    elements.append(Spacer(1, 24))
    elements.append(HRFlowable(width="100%", thickness=1, color=BORDER, spaceAfter=24))
    sign_data = [
        ["Prepared By", "Approved By", "Company Man / Witness"],
        ["", "", ""],
    ]
    elements.append(_table(sign_data, [56 * mm, 56 * mm, 56 * mm], header_bg=SECONDARY))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(
        "<i>This procedure sheet is generated automatically by PyMudCement-Optima. "
        "Field execution must follow the approved well programme.</i>",
        body_style,
    ))

    doc.build(elements)