from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root#$17",
    database="javalean_db"
)

@app.route("/")
def login():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def check_login():

    username = request.form["username"]
    password = request.form["password"]

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=%s AND password=%s",
        (username, password)
    )

    result = cursor.fetchone()

    if result:
        return render_template("home.html")
    else:
        return "Invalid username or password"

if __name__ == "__main__":
    app.run(debug=True)