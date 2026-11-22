# CodeAlpha Task 3 – Secure Coding Review

A Python Flask educational project that compares an intentionally vulnerable login
application with a more secure implementation.

## Features
- SQL injection demonstration
- Plaintext password storage demonstration
- Hardcoded demo credentials
- Input validation
- Password hashing
- Parameterized SQL queries
- Generic client-facing error messages
- Environment-based Flask secret key

## Requirements
- Python 3
- Windows, macOS, or Linux
- Flask and Werkzeug

## Setup (Windows CMD)

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run the vulnerable demonstration

```cmd
python vulnerable_app.py
```

Open http://127.0.0.1:5000

Local demo account:
- Username: `admin`
- Password: `admin123`

The vulnerable app is intentionally insecure. Keep it on localhost.

## Run the secure application

Stop the first server with `Ctrl+C`, then set a local development secret:

```cmd
set FLASK_SECRET_KEY=replace-this-with-a-long-random-development-secret
python secure_app.py
```

Open http://127.0.0.1:5001

Register a new account. Usernames must be 3–32 letters, numbers, or underscores.
Passwords must be 12–128 characters.

## Project files
- `vulnerable_app.py` – intentionally insecure local demonstration
- `secure_app.py` – corrected educational implementation
- `security_review.md` – findings, impacts, remediations, and test record
- `requirements.txt` – Python dependencies
- `screenshots/` – add your own genuine test screenshots here

## Security notice
Use only on your own computer. Do not expose the vulnerable app to a network or
test these techniques against systems without explicit authorization.

The secure app is a learning example, not production-ready authentication software.
See `security_review.md` for limitations and additional controls needed for deployment.

## Internship
CodeAlpha Cyber Security Internship

## Author
Balaganesh P
