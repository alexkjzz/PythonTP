
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from db import db

class User(db.Model, UserMixin):
    __tablename__ = 'Utilisateurs'

    ID_utilisateur = db.Column(Integer, primary_key=True)
    Nom = db.Column(String(50), nullable=False)
    Prenom = db.Column(String(50), nullable=False)
    Email = db.Column(String(100), unique=True, nullable=False)
    MDP = db.Column(String(100), nullable=False)
    ID_role = db.Column(Integer, nullable=False)

    def __init__(self, Nom, Prenom, Email, MDP, ID_role=0):
        self.Nom = Nom
        self.Prenom = Prenom
        self.Email = Email
        self.MDP = generate_password_hash(MDP)
        self.ID_role = ID_role

    def set_password(self, MDP):
        self.MDP = generate_password_hash(MDP)

    def check_password(self, MDP):
        return check_password_hash(self.MDP, MDP)

    def get_id(self):
        return str(self.ID_utilisateur)
