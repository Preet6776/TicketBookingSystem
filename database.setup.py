
import sqlite3

connection = sqlite3.connect("booking.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    seat_number INTEGER NOT NULL UNIQUE
)
""")

cursor.execute(
    "INSERT OR IGNORE INTO bookings (seat_number) VALUES (?)",
    (2,)
)

cursor.execute(
    "INSERT OR IGNORE INTO bookings (seat_number) VALUES (?)",
    (4,)
)

connection.commit()

cursor.execute("SELECT * FROM bookings")
bookings = cursor.fetchall()

print("Bookings stored in database:")
print(bookings)

connection.close()
