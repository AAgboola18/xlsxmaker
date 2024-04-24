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
    headers = list(df.colums)
    for i in range(len(headers)):
        headers[i] = headers[i].replace("_", " ")
        headers[i] = headers[i].title()

    pdf.set_font(family="Helvetica", style="B", size=12)
    pdf.cell(w=30, h=8, txt=headers[0], border=1)
    pdf.cell(w=59, h=8, txt=headers[1], border=1)
    pdf.cell(w=43, h=8, txt=headers[2], border=1)
    pdf.cell(w=33, h=8, txt=headers[3], border=1)
    pdf.cell(w=25, h=8, txt=headers[4], border=1, ln=1)

    for index,row in df.iterrows():
        pdf.set_font(family="Helvetica", size=12)
        pdf.set_text_colour(80, 80, 80)
        pdf.cell(w=59, h=8, txt=str(row["product_id"]), border=1)
        pdf.cell(w=43, h=8, txt=str(row["product_name"]), border=1)
        pdf.cell(w=33, h=8, txt=str(row["amount_purchased"]), border=1)
        pdf.cell(w=25, h=8, txt=str(row["price_per_unit"]), border=1)
        pdf.cell(w=25, h=8, txt=str(row["total_price"]), border=1, ln=1)



    pdf.output(f"PDFs/{filename}.pdf")
