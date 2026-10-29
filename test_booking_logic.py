
from booking_logic import is_valid_seat


def test_valid_seat():
    assert is_valid_seat(3) == True


def test_first_seat():
    assert is_valid_seat(1) == True


def test_last_seat():
    assert is_valid_seat(5) == True


def test_seat_zero():
    assert is_valid_seat(0) == False


def test_seat_too_high():
    assert is_valid_seat(6) == False

