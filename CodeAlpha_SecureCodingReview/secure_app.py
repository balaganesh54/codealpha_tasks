import os
import re
import sqlite3
from contextlib import contextmanager

from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError(
        "Set the FLASK_SECRET_KEY environment variable before starting the app."
    )

app.config["SECRET_KEY"] = SECRET_KEY
DATABASE = "secure.db"


@contextmanager
def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
    finally:
        connection.close()


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        """)


def valid_username(username):
    return bool(re.fullmatch(r"[A-Za-z0-9_]{3,32}", username))


@app.route("/", methods=["GET"])
def home():
    return """
    <h2>Secure Login Application</h2>
    <h3>Register</h3>
    <form method="POST" action="/register">
        <input name="username" placeholder="Username" required>
        <input name="password" type="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>
    <h3>Login</h3>
    <form method="POST" action="/login">
        <input name="username" placeholder="Username" required>
        <input name="password" type="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    """


@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if not valid_username(username):
        return "Invalid username format.", 400
    if len(password) < 12 or len(password) > 128:
        return "Password must be between 12 and 128 characters.", 400

    password_hash = generate_password_hash(password)

    try:
        with get_connection() as connection:
            connection.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, password_hash)
            )
        return "Registration successful. You can now log in."
    except sqlite3.IntegrityError:
        return "Unable to register with those details.", 400
    except sqlite3.Error:
        app.logger.exception("Database error during registration")
        return "A server error occurred.", 500


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")

    if not valid_username(username) or not password or len(password) > 128:
        return "Invalid username or password.", 401

    try:
        with get_connection() as connection:
            user = connection.execute(
                "SELECT password_hash FROM users WHERE username = ?",
                (username,)
            ).fetchone()

        if user and check_password_hash(user["password_hash"], password):
            return "Login successful."
        return "Invalid username or password.", 401
    except sqlite3.Error:
        app.logger.exception("Database error during login")
        return "A server error occurred.", 500


if __name__ == "__main__":
    initialize_database()
    # Localhost only; debug mode is disabled.
    app.run(host="127.0.0.1", port=5001, debug=False)
