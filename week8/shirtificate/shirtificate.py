from fpdf import FPDF


class PDF:
    # PDF Object Constructor (Makes PDF)
    def __init__(self, name):
        self._pdf = FPDF(orientation="P", unit="mm", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 30)
        # Creating pdf header
        self._pdf.cell(h=0, w=self._pdf.epw, txt="CS50 Shirtificate", align="C")
        # Calculating horizontal position of image
        x = (self._pdf.epw - 180) / 2
        # Creating & Centering the image
        self._pdf.image("shirtificate.png", x=x + 8, y=55, w=180)
        # Adding text to the center of the shirt
        self._pdf.set_font("helvetica")
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=60, y=140, txt=f"{name} took CS50")

    # Class method that outputs the pdf instance variable of the PDF class
    def save_pdf(self, name):
        self._pdf.output(name)


name = input("Name: ")
# Initialize a pdf object
pdf = PDF(name)
pdf.save_pdf("shirtificate.pdf")
