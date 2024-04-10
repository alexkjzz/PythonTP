# db.py

from flask_sqlalchemy import SQLAlchemy

# Configuration de la base de données
DB_CONFIG = {
    'HOST': 'your_database_host',
    'USER': 'your_database_user',
    'PASSWORD': 'your_database_password',
    'DB_NAME': 'your_database_name'
}

# Initialisation de l'extension SQLAlchemy
db = SQLAlchemy()

# Configuration de l'application Flask pour la base de données
def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{DB_CONFIG['USER']}:{DB_CONFIG['PASSWORD']}@{DB_CONFIG['HOST']}/{DB_CONFIG['DB_NAME']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
