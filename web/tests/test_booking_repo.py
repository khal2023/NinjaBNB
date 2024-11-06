from lib.users import Users
from lib.property import Property
from lib.booking_repo import BookingRepo
from lib.booking import Booking

def test_repo_instantiates(db_connection):
    connection = db_connection
    repo = BookingRepo(connection)
    assert repo._connection == connection

# As a user I want to book a property for some dates
def test_view_current_bookings(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepo(db_connection)
    assert repo.list() == [
        Booking(1, 1, 1, '2024-11-05', '2024-11-15', 'Unconfirmed'),
        Booking(2, 2, 1, '2024-11-05', '2024-11-15', 'Confirmed'),
        Booking(3, 1, 1, '2024-11-05', '2024-11-15', 'Confirmed')
    ]


# def test_user_can_book_a_property_if_available(db_connection):
#     connection = db_connection
#     repo = BookingRepo(connection)
#     repo.make_booking(1, 1, "2024-11-05", "2024-11-15")





# Booking repo user stories:
# BOOKERS
# 	
# 	- As a user I want to see if a property is available on certain dates
	
# OWNERS 
# 	- As a user I want to see pending bookings for my apartment
# As a user I want to approve or deny bookings for my apartment