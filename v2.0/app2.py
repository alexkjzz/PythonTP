# app.py

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from db import db, init_app
from models import User , Favori
from forms import RegistrationForm, LoginForm
import requests

app = Flask(__name__)
# Configuration secrète
app.config['SECRET_KEY'] = '08c12c9a83b5bc7e0ecf54b3d28dc1fc'

# Initialisation de la base de données
init_app(app)

# Initialisation de l'extension de gestion de connexion
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes de l'application
@app.route('/')
def index():
    return render_template('index.html')

from sqlalchemy.exc import SQLAlchemyError

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            new_user = User(username=form.username.data,firstname=form.firstname.data, email=form.email.data, password=form.password.data, role=0)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating account: {str(e)}', 'danger')
            print(f'Error creating account: {str(e)}')  # Ajoutez cette ligne pour afficher l'erreur dans la console
    else:
        print('Form is not valid')  # Ajoutez cette ligne pour déboguer si le formulaire n'est pas valide
    
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('dashboard'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')




# Fonction pour récupérer les films depuis SWAPI
def fetch_star_wars_films():
    url = "https://swapi.dev/api/films/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lève une exception en cas d'erreur HTTP

        film_data = response.json()['results']
        films = []

        for film in film_data:
            film_info = {
                'title': film['title'],
                'episode_id': film['episode_id'],
                'director': film['director'],
                'release_date': film['release_date']
                # Vous pouvez ajouter d'autres champs ici si nécessaire
            }
            films.append(film_info)

        return films

    except requests.exceptions.RequestException as e:
        print(f"Error fetching films from SWAPI: {str(e)}")
        return []


@app.route('/add_favorite', methods=['POST'])
@login_required
def add_favorite():
    film_title = request.form['film_title']
    episode_id = request.form['episode_id']

    favori = Favori(user_id=current_user.id, film_title=film_title, episode_id=episode_id)
    db.session.add(favori)
    db.session.commit()

    flash(f'{film_title} added to favorites!', 'success')
    return redirect(url_for('dashboard'))


# Exécution de l'application
if __name__ == '__main__':
    app.run(debug=True)
