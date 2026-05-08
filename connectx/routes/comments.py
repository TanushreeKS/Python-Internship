from flask import Blueprint, request, redirect
from flask_login import login_required, current_user
from extensions import mysql

comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/comment/<int:post_id>", methods=["POST"])
@login_required
def comment(post_id):

    content = request.form["content"]

    cur = mysql.connection.cursor()

    cur.execute("""
        INSERT INTO comments(user_id, post_id, content)
        VALUES(%s,%s,%s)
    """, (current_user.id, post_id, content))

    mysql.connection.commit()

    return redirect("/feed")