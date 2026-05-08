
from flask import Flask
from config import Config
from extensions import mysql, login_manager

from routes.auth import auth_bp
from routes.posts import posts_bp
from routes.comments import comments_bp
from routes.likes import likes_bp
from routes.profile import profile_bp
from routes.admin import admin_bp
from routes.follows import follows_bp
from routes.reports import reports_bp

from models.user import User

app = Flask(__name__)
app.config.from_object(Config)

mysql.init_app(app)
login_manager.init_app(app)

# IMPORTANT USER LOADER
@login_manager.user_loader
def load_user(user_id):

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM users WHERE id=%s", [user_id])

    user_data = cur.fetchone()

    if user_data:
        return User({
            "id": user_data[0],
            "username": user_data[1],
            "email": user_data[2],
            "password": user_data[3],
            "is_admin": user_data[6]
        })

    return None

app.register_blueprint(auth_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(comments_bp)
app.register_blueprint(likes_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(follows_bp)
app.register_blueprint(reports_bp)

if __name__ == "__main__":
    app.run(debug=True)