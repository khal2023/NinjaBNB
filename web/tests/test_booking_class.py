from lib.booking import Booking
def test_booking_class_instantiates_correctly():
    booking = Booking(1, 24, 5, "2024-11-05", "2024-11-15", "Unconfirmed")
    assert booking.id == 1
    assert booking.property_id == 24
    assert booking.user_id == 5
    assert booking.start_date == "2024-11-05"
    assert booking.end_date == "2024-11-15"
    assert booking.status == "Unconfirmed"

def test_booking_class_eq():
    booking1 = Booking(1, 24, 5, "2024-11-05", "2024-11-15", "Unconfirmed")
    booking2 = Booking(1, 24, 5, "2024-11-05", "2024-11-15", "Unconfirmed")

    assert booking1 == booking2

def test_booking_repr():
    booking = Booking(1, 24, 5, "2024-11-05", "2024-11-15", "Unconfirmed")
    assert str(booking) == "Booking(1, 24, 5, 2024-11-05, 2024-11-15, Unconfirmed)"


