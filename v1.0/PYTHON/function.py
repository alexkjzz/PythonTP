import urllib.request
import json

def fetch_swapi_data(url):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()
        return json.loads(data)

def fetch_all_films_info():
    films_info = []
    base_url = "https://swapi.dev/api/films/"

    # Récupérer les données pour chaque film
    for i in range(1, 7):  # Il y a 6 films dans l'API SWAPI
        url = base_url + str(i) + "/"
        data = fetch_swapi_data(url)
        film_info = {
            'title': data['title'],
            'episode_id': data['episode_id'],
            'director': data['director'],
            'release_date': data['release_date']
        }
        films_info.append(film_info)

    return films_info

# Récupérer toutes les informations sur les films
all_films_info = fetch_all_films_info()

# Afficher les informations récupérées
for film_info in all_films_info:
    print(film_info)



json_data = json.dumps(film_info)
