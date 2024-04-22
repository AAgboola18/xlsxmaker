import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath)

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_date, invoice_number = filename.split("-")

    pdf.set_font(family="Helvetica", style="B", size=16)
    pdf.cell(w=0, h=12, txt=f"Invoice number: {invoice_number}", ln=1,  align="R")
    headers = df.columns
    pdf.cell(w=30, h=8, txt=headers[0], border=1)
    pdf.cell(w=30, h=8, txt=headers[1], border=1)
    pdf.cell(w=30, h=8, txt=headers[2], border=1)
    pdf.cell(w=30, h=8, txt=headers[3], border=1)
    pdf.cell(w=30, h=8, txt=headers[4], border=1)
    pdf.output(f"PDFs/{filename}.pdf")
