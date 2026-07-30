from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(filename, sections):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph("<b>PyMudCement-Optima Report</b>", styles["Title"])
    )

    elements.append(
        Paragraph("Drilling Engineering Calculation Report", styles["Heading2"])
    )

    for title, data in sections.items():

        elements.append(
            Paragraph(f"<br/><b>{title}</b>", styles["Heading2"])
        )

        table_data = [["Parameter", "Value"]]

        for key, value in data.items():
            table_data.append([key, str(value)])

        table = Table(table_data)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("BACKGROUND", (0,1), (-1,-1), colors.beige),
            ("BOTTOMPADDING", (0,0), (-1,0), 10),
        ]))

        elements.append(table)

    doc.build(elements)