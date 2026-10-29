
import sqlite3
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

DATABASE_NAME = "booking.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row

    try:
        yield connection
    finally:
        connection.close()


@app.get("/")
def home():
    return {"message": "Welcome to Ticket Booking System"}


@app.post("/book/{seat_number}")
def book_seat(
    seat_number: int,
    connection: sqlite3.Connection = Depends(get_connection)
):
    if seat_number < 1 or seat_number > 5:
        raise HTTPException(
            status_code=400,
            detail="Invalid seat number"
        )

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM bookings WHERE seat_number = ?",
        (seat_number,)
    )

    if cursor.fetchone() is not None:
        raise HTTPException(
            status_code=409,
            detail="This seat is already booked"
        )

    cursor.execute(
        "INSERT INTO bookings (seat_number) VALUES (?)",
        (seat_number,)
    )

    connection.commit()

    return {
        "message": "Booking successful!",
        "seat_number": seat_number
    }
