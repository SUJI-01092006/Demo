from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        con.commit()

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# API to add user
@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.json.get("name")
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
        con.commit()
    return jsonify({"message": "User added successfully!"})

# API to get users
@app.route("/get_users")
def get_users():
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
    return jsonify(users)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
