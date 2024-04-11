# db.py

from flask_sqlalchemy import SQLAlchemy

# Configuration de la base de données
DB_CONFIG = {
    'DATABASE': '../BDD/python_bdd.bd'
}

# Initialisation de l'extension SQLAlchemy
db = SQLAlchemy()

# Configuration de l'application Flask pour la base de données
def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_CONFIG['DATABASE']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

