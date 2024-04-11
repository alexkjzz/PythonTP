
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from db import db

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    user_id = db.Column(Integer, primary_key=True)
    firstname = db.Column(String(50), nullable=False)
    username = db.Column(String(50), nullable=False)
    email = db.Column(String(100), unique=True, nullable=False)
    password = db.Column(String(100), nullable=False)
    role = db.Column(Integer, nullable=False)

    def __init__(self, username,email,firstname, password, role=0):
        self.username = username
        self.firstname = firstname
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

    user_id = db.Column(Integer, db.ForeignKey('user.user_id'), primary_key=True)  # Clé étrangère vers user_id
    film_title = db.Column(String(255), primary_key=True)
    episode_id = db.Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Favori {self.film_title}>"