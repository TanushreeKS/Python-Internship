from flask import Blueprint, redirect
from flask_login import login_required, current_user
from extensions import mysql

likes_bp = Blueprint("likes", __name__)

@likes_bp.route("/like/<int:post_id>")
@login_required
def like(post_id):

    cur = mysql.connection.cursor()

    try:
        cur.execute("""
            INSERT INTO likes(user_id, post_id)
            VALUES(%s,%s)
        """, (current_user.id, post_id))

        mysql.connection.commit()

    except:
        pass

    return redirect("/feed")