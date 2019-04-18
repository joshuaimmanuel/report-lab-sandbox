from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    Table,
    Frame,
)
from reportlab.lib.units import cm, inch
from reportlab.rl_config import canvas_basefontname
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.colors import pink, red, blue

from reportlab.lib.styles import (
    getSampleStyleSheet,
    StyleSheet1,
    ParagraphStyle,
)
stylesheet=getSampleStyleSheet()
normalStyle = stylesheet['Normal']

def _construct_header():
    header = []

    name_style = ParagraphStyle(
        name='name', fontName="Times", fontSize=20, leading=20*1.2,
        alignment=TA_CENTER)
    aff_style = ParagraphStyle(
        name='aff_style', fontName="Times", fontSize=10, alignment=TA_CENTER,
        leading=10*1.2)
    rank_style = ParagraphStyle(
        name='rank_style', fontName="Times", fontSize=12, alignment=TA_CENTER,
        leading=12*1.2)
    app_style = ParagraphStyle(
        name='app_style', fontName="Times", fontSize=14, alignment=TA_CENTER,
        leading=14*1.2)

    logo_img = Image("logo-color-tc-arts.png", 2.8*cm, 2.8*cm)
    logo_img.hAlign = TA_CENTER
    year_img = Image("70-years.png", 2*cm, 2*cm)
    name = Paragraph("THIAGARAJAR COLLEGE, MADURAI - 09", name_style)

    desc = Paragraph(
        "(An Autonomous Institution affliated to Madurai Kamaraj University)",
        aff_style)
    agg = Paragraph("(Re-Accredited with 'A' Grade by NAAC)", aff_style)
    rank = Paragraph("Ranked 34th in NIRF 2019", rank_style)
    app = Paragraph("APPLICATION FOR ADMISSION 2019-2020", app_style)

    w, h = A4
    li = []
    li.append((logo_img, [name, desc, agg, rank, app], year_img))
    tbl = Table(li, [3*cm, w-7.1*cm, 2.5*cm], style=[
        # ('SPAN', (0, 0), (2, 0)),
        ('ALIGN', (0, 0), (0, 0), 'RIGHT'),
        ('ALIGN', (1, 0), (1, 0), 'LEFT'),
        ('VALIGN', (1, 0), (1, 0), 'TOP'),
        ('VALIGN', (2, 0), (2, 0), 'MIDDLE'),
        # ('BACKGROUND', (1, 0), (1, 0), pink),
        # ('BACKGROUND', (0, 0), (0, 0), red),
        # ('BACKGROUND', (2, 0), (2, 0), blue),
    ])
    return tbl

def _construct_body():
    contents = []
    style = ParagraphStyle(
        name='rank_style', fontName="Times", fontSize=12, alignment=TA_LEFT,
        leading=12*2)

    w, h = A4
    li = []
    li.append((Paragraph("Application No.", style),
               Paragraph(": <b>57727</b>", style)))
    li.append((Paragraph("Category", style),
               Paragraph(": <b>Aided</b>", style)))
    li.append((Paragraph("Degree", style), Paragraph(": <b>B.A.</b>", style)))
    li.append((Paragraph("Major", style), Paragraph(": <b>Tamil</b>", style)))
    li.append((Paragraph("Name", style), Paragraph(": <b>John Doe</b>", style)))
    li.append((Paragraph("Gender", style), Paragraph(": <b>Male</b>", style)))
    li.append((Paragraph("Date of birth", style),
               Paragraph(": <b>20/05/2003</b>", style)))
    li.append((Paragraph("Community", style), Paragraph(": <b>BC</b>", style)))
    li.append((Paragraph("Stream", style),
               Paragraph(": <b>Vocational</b>", style)))
    li.append((Paragraph("Board", style), Paragraph(": <b>State</b>", style)))
    li.append((Paragraph("Month and year of passing", style),
               Paragraph(": <b>Apr 2019</b>", style)))
    li.append((Paragraph("Marks scored", style),
               Paragraph(": <b>1190 / 1200</b>", style)))
    li.append((Paragraph("Differently abled", style),
               Paragraph(": <b>No</b>", style)))
    li.append((Paragraph("Son/Daughter of Ex-Service man of Tamil origin",
                         style),
               Paragraph(": <b>No</b>", style)))
    li.append((Paragraph("Tamil origin from Andaman Nichobar Islands", style),
               Paragraph(": <b>No</b>", style)))
    li.append((Paragraph("Outstanding sports certificate", style),
               Paragraph(": <b>Yes</b> (District level)", style)))
    li.append((Paragraph("Require hostel accommodation", style),
               Paragraph(": <b>No</b>", style)))
    li.append((Paragraph("Application Fees", style),
               Paragraph(": <b>Waived off</b>", style)))
    li.append((Paragraph("Payment status", style),
               Paragraph(": <b>Not applicable</b>", style)))
    half = w/2
    tbl = Table(li, [half-4.5*cm, half-5*cm], style=[
         ('BACKGROUND', (1, 0), (1, 0), pink),
         ('BACKGROUND', (0, 0), (0, 0), red),
        ])
    return tbl
def generate_report():
    doc = SimpleDocTemplate("form.pdf", pagesize=A4, topMargin=1*cm,
                            bottomMargin=1*cm, leftMargin=2*cm,
                            rightMargin=2*cm)
    story = []
    story.append(_construct_header())
    story.append(Spacer(inch, cm))
    story.append(_construct_body())
    doc.build(story)


if __name__ == "__main__":
    generate_report()
