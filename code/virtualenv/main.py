from datetime import datetime
import random
all_flights = [ 
#   ['Unique_ID', 'To', 'From', Dept_datetime, Arrival_datetime, 'Departure_airport_code', 'Arrival_Airport_Code', 'Delayed_Departure_time', 'Delayed_Arrival_Time', {'Economy':('total_seats', 'price', 'luggage_allowance'), 'Premium_Economy':('total_seats', 'price', 'luggage_allowance'), 'Business':('total_seats', 'price', 'luggage_allowance'), 'First':('total_seats', 'price', 'luggage_allowance')}, 'Flght_Number', 'Aircraft_type', 'Emissions', 'International(Boolean), '[Passenger_List]']
    [
    '2030404003'
    'Singapore', 'Beijing', 
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
    ['SampleUser1', 'Formula1', None, None, None, 'Test', '123', 'test@email.com', '30303030']
]

def BookFlight_Backend(flight_number, ):
    return