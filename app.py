import sqlite3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

DATABASE = "database/stylehub.db"

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        mobile TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/api/users/register", methods=["POST"])
def register():

    data = request.get_json()

    name = data.get("name")
    mobile = data.get("mobile")
    password = data.get("password")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, mobile, password) VALUES (?, ?, ?)",
        (name, mobile, password)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": "Account Created Successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    create_database()
    app.run(debug=True)