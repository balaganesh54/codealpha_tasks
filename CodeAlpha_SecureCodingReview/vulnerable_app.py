import sqlite3
from flask import Flask, request

app = Flask(__name__)
DATABASE = "vulnerable.db"

# Intentionally insecure demonstration credentials.
DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin123"


def initialize_database():
    with sqlite3.connect(DATABASE) as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT
            )
        """)
        exists = connection.execute(
            "SELECT id FROM users WHERE username = ?",
            (DEFAULT_USERNAME,)
        ).fetchone()
        if exists is None:
            connection.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (DEFAULT_USERNAME, DEFAULT_PASSWORD)
            )


@app.route("/", methods=["GET"])
def home():
    return """
    <h2>Vulnerable Login Application</h2>
    <form method="POST" action="/login">
        <input name="username" placeholder="Username" required>
        <br><br>
        <input name="password" type="password" placeholder="Password" required>
        <br><br>
        <button type="submit">Login</button>
    </form>
    <p>Local demo account: admin / admin123</p>
    """


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    connection = sqlite3.connect(DATABASE)
    try:
        cursor = connection.cursor()

        # INTENTIONALLY VULNERABLE: unsafe SQL string concatenation.
        query = (
            "SELECT * FROM users WHERE username = '"
            + username
            + "' AND password = '"
            + password
            + "'"
        )
        cursor.execute(query)
        user = cursor.fetchone()

        if user:
            return "<h2>Login successful</h2><p>Welcome!</p>"
        return "<h2>Invalid username or password</h2>", 401

    except sqlite3.Error as error:
        # INTENTIONALLY INSECURE: detailed database error disclosure.
        return f"Database error: {error}", 500
    finally:
        connection.close()


if __name__ == "__main__":
    initialize_database()
    # Localhost only; do not expose this intentionally vulnerable app.
    app.run(host="127.0.0.1", port=5000, debug=False)
