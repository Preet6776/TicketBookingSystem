
import sqlite3
import pytest
from fastapi.testclient import TestClient
from main import app, get_connection


@pytest.fixture
def test_db():
    connection = sqlite3.connect(
        ":memory:",
        check_same_thread=False
    )

    connection.execute("""
        CREATE TABLE bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seat_number INTEGER NOT NULL UNIQUE
        )
    """)

    connection.commit()

    yield connection

    connection.close()


@pytest.fixture
def client(test_db):
    def override_get_connection():
        yield test_db

    app.dependency_overrides[get_connection] = override_get_connection

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Welcome to Ticket Booking System"
    }


def test_invalid_seat(client):
    response = client.post("/book/6")

    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid seat number"
    }


def test_available_seat_booking(client, test_db):

    response = client.post("/book/3")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Booking successful!",
        "seat_number": 3
    }

    result = test_db.execute(
        "SELECT seat_number FROM bookings WHERE seat_number = 3"
    ).fetchone()

    assert result == (3,)

def test_duplicate_seat_booking(client):
    # First booking
    first_response = client.post("/book/3")

    assert first_response.status_code == 200

    # Try booking the same seat again
    second_response = client.post("/book/3")

    assert second_response.status_code == 409
    assert second_response.json() == {
        "detail": "This seat is already booked"
    }
