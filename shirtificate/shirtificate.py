from fpdf import FPDF

name = input("Name: ")

class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("shirtificate.png", 30, 60, 150)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 30)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 10, "CS50 Shirtificate", border=0, align="C")
        # Performing a line break:
        self.ln(20)

    def footer(self):
        # Setting font: helvetica italic 8
        self.set_font("helvetica", "B", 20)
        self.set_text_color(255, 255, 255)
        self.cell(80)
        self.cell(30, 150, f"{name} took CS50", border=0, align="C")
        self.ln(20)

pdf = PDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 30)
pdf.output("shirtificate.pdf")