# db.py

from flask_sqlalchemy import SQLAlchemy
import os

db_path = os.path.join(os.path.dirname(__file__), 'BDD/python_bdd.db')

# Configuration de la base de données

# Initialisation de l'extension SQLAlchemy
db = SQLAlchemy()

# Configuration de l'application Flask pour la base de données
def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

