
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from db import db

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    user_id = db.Column(Integer, primary_key=True)
    username = db.Column(String(50), nullable=False)
    email = db.Column(String(100), unique=True, nullable=False)
    password = db.Column(String(100), nullable=False)
    role = db.Column(Integer, nullable=False)

    def __init__(self, username,email, password, role=0):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return str(self.user_id)


class Favori(db.Model):
    __tablename__ = 'favoris'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    film_title = db.Column(db.String(255), nullable=False)
    episode_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Favori {self.film_title}>"