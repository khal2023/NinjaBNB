from lib.booking import Booking
from datetime import datetime, timedelta

class BookingRepo:
    def __init__(self, connection):
        self._connection = connection
    
    def list(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        return [Booking(row["id"], row["property_id"], row["user_id"], row["b_start_date"], row["b_end_date"], row["b_status"]) for row in rows]

    def make_booking(self, username, property_name, start_date, end_date):
    
        if self.date_clash_found(property_name, start_date, end_date):
            raise Exception(f"Sorry, {property_name} are booked during those dates!")
        
        if self.user_owns_property(username, property_name):
            raise Exception("You can't book a property you own!")
        
        user_rows = self._connection.execute('SELECT id FROM users WHERE username = %s', [username])
        property_rows = self._connection.execute('SELECT id FROM properties WHERE property_name = %s', [property_name])
        self._connection.execute("INSERT INTO bookings (property_id, user_id, b_start_date, b_end_date, b_status) VALUES (%s, %s, %s, %s, 'Unconfirmed')", [
            property_rows[0]["id"], user_rows[0]["id"], start_date, end_date])
    
    def get_price_of_booking(self, property_name, start_date, end_date):
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        prices = self._connection.execute('SELECT price_per_night FROM properties WHERE property_name = %s', [property_name])
        return (end - start).days * prices[0]["price_per_night"]
        

# VALIDITY CHECKS
        
    def date_clash_found(self, property_name, start_date, end_date):
        booked_dates = self._connection.execute(
            '''SELECT generate_series(b_start_date, b_end_date, '1 day'::INTERVAL)::DATE AS DATE
                FROM
                (SELECT b_start_date, b_end_date 
                FROM bookings 
                WHERE property_id = 
                    (SELECT id 
                    FROM properties
                    WHERE property_name = %s))''', [property_name])
        required_dates = self._connection.execute("SELECT generate_series(%s, %s, '1 day'::INTERVAL):: DATE AS DATE", [
            start_date, end_date
        ])
        return any(date in required_dates for date in booked_dates)
    
    def user_owns_property(self, username, property_name):
        property_owner_id = self._connection.execute('SELECT host_id FROM properties WHERE property_name = %s', [property_name])
        user_id = self._connection.execute('SELECT id FROM users WHERE username = %s', [username])
        return property_owner_id[0]["host_id"] == user_id[0]["id"]
    
    def end_date_before_start_date(start_date, end_date):
        pass
    
    def start_date_before_today(start_date):
        pass