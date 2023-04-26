import io
import os
import barcode
import qrcode
from barcode import Code128
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm, cm
from reportlab.lib import colors
from barcode.writer import ImageWriter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def create_ticket(place, venue, timelabel, time, namelabel, name, eventlabel, eventname, logo_file, barcode_value):
    # Define the PDF file buffer
    buffer = io.BytesIO()
    
    # Define the canvas and set the page size and orientation
    c = canvas.Canvas(buffer, pagesize=landscape(A4))
    
    # Set the logo image
    logo = ImageReader(logo_file)
    
    # Define the font styles
    styles = {
        'Normal': ParagraphStyle(
            'normal',
            fontName='Helvetica',
            fontSize=18,
            leading=22,
            textColor='black',
            alignment=TA_CENTER,
        ),
        'Bold': ParagraphStyle(
            'bold',
            fontName='Helvetica-Bold',
            fontSize=18,
            leading=22,
            textColor='black',
            alignment=TA_CENTER,
        ),
        'Heading1': ParagraphStyle(
            'heading1',
            fontName='Helvetica',
            fontSize=28,
            leading=36,
            textColor='black',
            alignment=TA_CENTER,
        ),
        'Heading2': ParagraphStyle(
            'heading2',
            fontName='Helvetica',
            fontSize=20,
            leading=28,
            textColor='black',
            alignment=TA_CENTER,
        ),
    }
    
    # Define the barcode
    barcode_value = str(barcode_value)
    barcode_value = barcode_value.rjust(10, '0') # Pad the barcode with leading zeros
    barcode_image = Code128(barcode_value, writer=ImageWriter())

    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(barcode_value)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save('qr.png')
    
    # Define the layout and content of the ticket
    c.setFillColor(colors.black)
    c.drawImage(logo, 1*cm, 15*cm, width=5*cm, height=5*cm)
    c.setFont(styles['Heading1'].fontName, 28)
    c.drawCentredString(16.85*cm, 18*cm, eventlabel)
    c.drawCentredString(16.85*cm, 16.8*cm, eventname)
    c.setFont(styles['Normal'].fontName, 18)
    c.drawCentredString(16.85*cm, 15*cm, place)
    c.drawCentredString(16.85*cm, 14.2*cm, venue)
    c.drawCentredString(16.85*cm, 13*cm, timelabel)
    c.drawCentredString(16.85*cm, 12.2*cm, time)
    c.drawCentredString(16.85*cm, 11*cm, namelabel)
    c.drawCentredString(16.85*cm, 10.2*cm, name)
    barcode_image.save('barcode')
    c.drawImage('barcode.png', 1*cm, 2*cm, width=5*cm, height=5*cm)
    c.drawImage('qr.png', 0.5*cm, 8*cm, width=6*cm, height=6*cm)
    c.setFont(styles['Bold'].fontName, 14)
    c.drawCentredString(16.85*cm, 3*cm, barcode_value)
    
    # Save the PDF file
    c.save()
    
    # Reset the buffer position to the beginning
    buffer.seek(0)
    
    # Return the PDF file buffer
    return buffer

# Define the ticket information
place = "Festival Venue"
venue = "{ Venue Name }"
timelabel = "Date & time:"
time = "{ Saturday, April 30, 2023 at 7:00 PM }"
namelabel = "Customer:"
name = "{ TrifectaFest }"
eventlabel = "Event"
eventname = "Trifectafest"
logo_file = "logo.png"
barcode_value = 1234567895

# Create the ticket PDF file
pdf_file = create_ticket(place, venue, timelabel, time, namelabel, name, eventlabel, eventname, logo_file, barcode_value)

# Write the PDF file to disk
with open('ticket.pdf', 'wb') as f:
    f.write(pdf_file.read())

