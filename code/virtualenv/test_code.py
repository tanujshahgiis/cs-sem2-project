import os
from datetime import datetime
from fpdf import FPDF
import barcode
from barcode.writer import ImageWriter
from PIL import Image

class TicketPDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Airline Ticket', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

# Create instance of FPDF class
pdf = TicketPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size = 12)

# Add ticket details
ticket_info = {
    "Passenger Name": "John Doe",
    "Flight Number": "AB123",
    "Departure": "Los Angeles (LAX)",
    "Destination": "New York (JFK)",
    "Departure Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
    "Seat": "12A",
    "Gate": "B22",
    "Boarding Time": "12:30 PM"
}

# Add details to PDF
for key, value in ticket_info.items():
    pdf.cell(200, 10, txt = f"{key}: {value}", ln = True, align = 'L')

# Generate a barcode
barcode_value = "123456789012"  # Example barcode value
ean = barcode.get('ean13', barcode_value, writer=ImageWriter())
barcode_filename = ean.save('barcode')

# Open the barcode image and paste it into the PDF
barcode_img = Image.open(f"{barcode_filename}")
pdf.image(f"{barcode_filename}", x=10, y=pdf.get_y() + 10, w=100)

# Save the PDF with name .pdf
pdf_filename = "airline_ticket_with_barcode.pdf"
pdf.output(pdf_filename)

# Open the PDF file
if os.name == 'nt':
    os.startfile(pdf_filename)
elif os.name == 'posix':
    os.system(f"xdg-open {pdf_filename}")
else:
    os.system(f"open {pdf_filename}")

print("PDF with barcode created and opened successfully!")
