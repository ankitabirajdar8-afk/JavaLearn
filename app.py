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


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )

        db.commit()

        return "Registration successful! You can now login."

    return render_template("register.html")


@app.route("/sem1")
def sem1():
    return render_template("sem1.html")


@app.route("/sem2")
def sem2():
    return render_template("sem2.html")


if __name__ == "__main__":
    app.run(debug=True)