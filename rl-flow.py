from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
)
from reportlab.lib.units import cm, inch
from reportlab.lib.styles import getSampleStyleSheet
stylesheet=getSampleStyleSheet()
normalStyle = stylesheet['Normal']

def _construct_header():
    header = []
    img = Image("logo-color-tc-arts.png", 3.5*cm, 3.5*cm)
    name = Paragraph("THIAGARAJAR COLLEGE, MADURAI - 09", normalStyle)
    desc = Paragraph(
        "(An Autonomous Institution affliated to Madurai Kamaraj University)",
        normalStyle)
    agg = Paragraph("(Re-Accredited with 'A' Grade by NAAC)", normalStyle)
    app = Paragraph("APPLICATION FOR ADMISSION 2018-2019", normalStyle)
    prog = Paragraph("UNDERGRADUATE COURSE", normalStyle)
    header.append((img, name))
    header.append(("", desc))
    header.append(("", agg))
    header.append(("", app))
    header.append(("", prog))
    tbl = Table(header, style=[('SPAN', (0, 0), (0, 4)),])
    return tbl

def generate_report():
    doc = SimpleDocTemplate("form.pdf", pagesize=A4, topMargin=2.5,
                            bottomMargin=2.5)
    Story = []

    Story.append(_construct_header())
    doc.build(Story)


if __name__ == "__main__":
    generate_report()
