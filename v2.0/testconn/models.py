from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from db import db  # Importez votre objet de base de données depuis le module approprié

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)