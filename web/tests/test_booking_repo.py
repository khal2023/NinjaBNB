from lib.users import Users
from lib.property import Property
from lib.booking_repo import BookingRepo
from lib.booking import Booking
import pytest

def test_repo_instantiates(db_connection):
    connection = db_connection
    repo = BookingRepo(connection)
    assert repo._connection == connection

# As a user I want to book a property for some dates
def test_view_current_bookings(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepo(db_connection)
    assert repo.list() == [
        Booking(1, 1, 1, '2024-09-05', '2024-09-15', 'Unconfirmed'),
        Booking(2, 2, 1, '2024-10-05', '2024-10-15', 'Confirmed'),
        Booking(3, 1, 1, '2024-11-05', '2024-11-15', 'Confirmed')
    ]

def test_user_can_book_a_property_if_available(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepo(db_connection)
    repo.make_booking("KHam", "The Laurels", "2024-12-05", "2024-12-15",)
    assert repo.list() == [
        Booking(1, 1, 1, '2024-09-05', '2024-09-15', 'Unconfirmed'),
        Booking(2, 2, 1, '2024-10-05', '2024-10-15', 'Confirmed'),
        Booking(3, 1, 1, '2024-11-05', '2024-11-15', 'Confirmed'),
        Booking(4, 2, 1, '2024-12-05', '2024-12-15', 'Unconfirmed')
    ]

def test_error_is_raised_if_booking_dates_clash(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepo(db_connection)
    with pytest.raises(Exception) as e:
        repo.make_booking("KHam", "The Laurels", "2024-10-05", "2024-10-17")
    assert str(e.value) == "Sorry, The Laurels are booked during those dates!"

def test_owner_cant_book_property_they_own(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepo(db_connection)
    with pytest.raises(Exception) as e:
        repo.make_booking("KHam", "The Ferns", "2024-12-05", "2024-12-15")
    assert str(e.value) == "You can't book a property you own!"

def test_price_of_potential_booking_is_returned(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepo(db_connection)
    assert repo.get_price_of_booking("The Ferns", "2024-12-05", "2024-12-10") == 250


def test_refuse_booking_if_end_before_start(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepo(db_connection)
    with pytest.raises(Exception) as e:
        repo.make_booking("KHam", "The Pines", "2024-12-05", "2024-11-15")
    assert str(e.value) == "Start date must be before end date"

def test_refuse_booking_if_start_before_today(db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    repo = BookingRepo(db_connection)
    with pytest.raises(Exception) as e:
        repo.make_booking("KHam", "The Pines", "2024-08-15", "2024-11-15")
    assert str(e.value) == "Start date must be from today"






# Booking repo user stories:
# BOOKERS
# 	
# 	- As a user I want to see if a property is available on certain dates
#   - see how much my booking will cost

	
# OWNERS 
# 	- As a user I want to see pending bookings for my apartment
# As a user I want to approve or deny bookings for my apartment