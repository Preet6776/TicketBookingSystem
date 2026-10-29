

\# Ticket Booking System



\## Project Description

A simple ticket booking application built using Python, SQLite, and FastAPI.



Users can book seats through the API. The system checks seat validity and prevents duplicate bookings.



\## Technologies Used

\- Python

\- SQLite

\- FastAPI

\- Pytest



\## Features

\- Validate seat numbers from 1 to 5

\- Book an available seat

\- Prevent duplicate seat bookings

\- Store booking information in SQLite

\- Test API endpoints and booking logic



\## Testing

Automated tests are written using Pytest.



Current test results:

\- API tests: 4

\- Booking logic tests: 5

\- Database tests: 1

\- Total: 10 tests passed



\## How to Run



Install the required packages:



```bash

py -m pip install fastapi uvicorn pytest httpx

```



Start the API server:



```bash

py -m uvicorn main:app --reload

```



Open the API documentation in your browser:



http://127.0.0.1:8000/docs



\## How to Run Tests



```bash

py -m pytest -v

```



