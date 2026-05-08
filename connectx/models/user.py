from flask_login import UserMixin
from extensions import mysql

class User(UserMixin):
    def __init__(self, data):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
        self.password = data['password']
        self.is_admin = data['is_admin']