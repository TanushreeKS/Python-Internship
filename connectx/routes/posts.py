from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from extensions import mysql

posts_bp = Blueprint("posts", __name__)

@posts_bp.route("/feed")
@login_required
def feed():

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT posts.id, posts.content,
               users.username,
               posts.created_at
        FROM posts
        JOIN users ON posts.user_id = users.id
        ORDER BY posts.created_at DESC
    """)

    posts = cur.fetchall()

    return render_template("feed.html", posts=posts)

@posts_bp.route("/create-post", methods=["POST"])
@login_required
def create_post():

    content = request.form["content"]

    cur = mysql.connection.cursor()

    cur.execute("""
        INSERT INTO posts(user_id, content)
        VALUES(%s,%s)
    """, (current_user.id, content))

    mysql.connection.commit()

    return redirect("/feed")