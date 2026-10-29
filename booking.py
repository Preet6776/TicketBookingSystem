
import sqlite3


def is_valid_seat(seat_number):
    if seat_number >= 1 and seat_number <= 5:
        return True
    else:
        return False

total_seats = 5

connection = sqlite3.connect("booking.db")
cursor = connection.cursor()

while True:
    user_input = input("Enter seat number (1-5) or q to quit: ")

    if user_input.lower() == "q":
        print("Thank you for using Ticket Booking!")
        break

    try:
        seat_number = int(user_input)

        if not is_valid_seat(seat_number):
            print("Invalid seat number")
            continue

        cursor.execute(
            "SELECT id FROM bookings WHERE seat_number = ?",
            (seat_number,)
        )

        if cursor.fetchone() is not None:
            print("Sorry, this seat is already booked.")
        else:
            cursor.execute(
                "INSERT INTO bookings (seat_number) VALUES (?)",
                (seat_number,)
            )
            connection.commit()
            print("Booking successful!")

    except ValueError:
        print("Please enter numbers only.")

connection.close()
