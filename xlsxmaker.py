import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath)
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    Filename = Path(filepath).stem

    pdf.set_font(family="Helvetica", style="B", size=16)
    pdf.cell(w=0, h=12, txt="Invoice number: ")
