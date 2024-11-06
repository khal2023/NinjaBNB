from lib.booking import Booking

class BookingRepo:
    def __init__(self, connection):
        self._connection = connection
    
    def list(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        return [Booking(row["id"], row["property_id"], row["user_id"], row["b_start_date"], row["b_end_date"], row["b_status"]) for row in rows]

