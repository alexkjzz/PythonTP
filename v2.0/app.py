from flask import Flask, render_template
import requests

app = Flask(__name__)

def fetch_films():
    try:
        response = requests.get('https://swapi.dev/api/films/')
        if response.status_code == 200:
            films_data = response.json()['results']
            filtered_films = [
                {'title': film['title'], 'episode_id': film['episode_id'], 'director': film['director']}
                for film in films_data
            ]
            return filtered_films
        else:
            print('Erreur lors de la récupération des données des films:', response.status_code)
            return []
    except Exception as e:
        print('Erreur lors de la récupération des données des films:', str(e))
        return []

@app.route("/")
def index():
    films = fetch_films()
    return render_template("index.php", films=films)

@app.route("/film_list")
def film_list():
    films = fetch_films()
    return render_template("film_list.html", films=films)

if __name__ == "__main__":
    app.run(debug=True)
