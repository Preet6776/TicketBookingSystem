import sqlite3


def test_booking_is_stored():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seat_number INTEGER NOT NULL UNIQUE
        )
    """)

    cursor.execute(
        "INSERT INTO bookings (seat_number) VALUES (?)",
        (3,)
    )

    cursor.execute("SELECT seat_number FROM bookings")
    result = cursor.fetchone()

    assert result == (3,)

    connection.close()