from datetime import datetime
import random
import os
import platform
from fpdf import FPDF
import barcode
from barcode.writer import ImageWriter
from PIL import Image
all_flights = [ 
#   ['Unique_ID', 'To', 'From', Dept_datetime, Arrival_datetime, 'Departure_airport_code', 'Arrival_Airport_Code', 'Delayed_Departure_time', 'Delayed_Arrival_Time', {'Economy':('total_seats', 'price', 'luggage_allowance'), 'Premium_Economy':('total_seats', 'price', 'luggage_allowance'), 'Business':('total_seats', 'price', 'luggage_allowance'), 'First':('total_seats', 'price', 'luggage_allowance')}, 'Flght_Number', 'Aircraft_type', 'Emissions', 'International(Boolean), '[Passenger_List]']
    [
    '2030404003'
    'Singapore', 
    'Beijing', 
     datetime(2024, 12, 5, 13, 30, 0), 
     datetime(2024, 12, 5, 16, 30, 0), 
    'SIN', 
    'DEL', 
    None, 
     None, 
     {'Economy':('150','400', '30 Kg'), 'Premium_Economy': None, 'Business': ('30','700', '50 Kg'), 'First': None}, 
     'SQ36', 
     'Airbus A350-900', 
     '300', 
     True, 
     [
        ['Passenger_given_name', 'Passenger_Last_Name', 'E-Ticket_No', 'Passenger Name Record (PNR)', 'Date_of_birth', 'Passport_No', 'Visa_No', 'Frequent_Flyer_No', 'Seat', 'Meal', 'Wheelchair', 'Luggage_Allowance' 'class', 'booking_datetime'],
        ['Tanuj', 'Shah', '1234567809', 'S0A5J2', datetime(2009,1,5), 'V103223', '40403020404022', None, '31A', 'Indian Veg Meal', False, '30 Kg', 'Economy', datetime(2024,12,4,23,40,0)]
     
     
     
     ]
     
     
    ]
     
]
user_data = [

#   ['Username', 'Password', [Prev_ticket_nos], [Active_tickets_nos], 'Locked_price', 'First_Name', 'Last_Name', 'Email_ID', 'Phone_no']
    ['SampleUser1', 'Formula1', None, None, None, 'Test', '123', 'test@email.com', '30303030', "user_id"]
]

def BookFlight_Backend(unique_id, user_id, airline_class, seat, pnr, passenger_given_name, passenger_last_name, passport_no, meal, wheelchair, dob, FF):
    for i in all_flights:
        if i[0] == unique_id:
            flight_exists = True
            flight_data = i 
            break
        else:
            flight_exists = False
            
    for i in user_data:
        if user_id in i[9]:
            user_valid = True
            break
        else:
            user_valid = False
        
    if airline_class in flight_data[9].keys():
        seats_occupied_for_that_class = 0
        for i in flight_data[14]:
            if i[12] == airline_class:
                seats_occupied_for_that_class += 1
        total_seats = flight_data[9][airline_class][0]
        seats_available = total_seats - seats_occupied_for_that_class
        if seats_available >= 1:
            seat_available_for_booking = True
    if passport_no != None and passenger_given_name != None and seat_available_for_booking == True and user_valid == True and flight_exists == True:
        class TicketPDF(FPDF):
            def header(self):
                self.set_font('Arial', 'B', 12)
                self.cell(0, 10, 'Global Airlines Ticket', 0, 1, 'C')
                self.ln(10)

            def footer(self):
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, 'E-Ticket', 0, 0, 'C')

# Create instance of FPDF class
        pdf = TicketPDF()

# Add a page
        pdf.add_page()

# Set font
        pdf.set_font("Arial", size = 12)

# Add ticket details
        ticket_info = {
            "Ticket Number" : '2342',
            "Passenger Name": passenger_given_name+passenger_last_name,
            "Flight Number": flight_data[10],
            "Departure": f"{flight_data[1]} ({flight_data[5]})",
            "Destination": f"{flight_data[2]} ({flight_data[6]})",
            "Departure Date and Time": flight_data[3],
            "Arrival Date and Time" : flight_data[4],
            "Class" : airline_class,
            

            
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
        pdf_filename = passenger_given_name
        pdf.output(pdf_filename)

# Open the PDF file
        if os.name == 'nt':
            os.startfile(pdf_filename)
        elif os.name == 'posix':
            os.system(f"xdg-open {pdf_filename}")
        else:
            os.system(f"open {pdf_filename}")


