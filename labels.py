# labels.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_label_pdf(tecidos: list[Tecido], filename: str):
    c = canvas.Canvas(filename, pagesize=A4)
    for tecido in tecidos:
        c.drawString(10, 800, f"Rolo: {tecido.numero_rolo.zfill(10)}")
        c.drawString(10, 780, f"Metros: {tecido.metros:.5f}")
        # ... outros campos
        c.showPage()
    c.save()