from flask import Blueprint, render_template, request, redirect, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from extensions import mysql
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def home():
    return render_template("index.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        cur = mysql.connection.cursor()

        cur.execute("""
            INSERT INTO users(username, email, password)
            VALUES(%s,%s,%s)
        """, (username, email, password))

        mysql.connection.commit()
        cur.close()

        flash("Registration successful")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email=%s", [email])

        user_data = cur.fetchone()

        if user_data:
            user = User({
                "id": user_data[0],
                "username": user_data[1],
                "email": user_data[2],
                "password": user_data[3],
                "is_admin": user_data[6]
            })

            if check_password_hash(user.password, password):
                login_user(user)

                if user.is_admin:
                    return redirect("/admin/dashboard")

                return redirect("/feed")

        flash("Invalid credentials")

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect("/")