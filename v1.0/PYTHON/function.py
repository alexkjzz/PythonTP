import urllib.request
import json

def fetch_swapi_data(url):
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()
        return json.loads(data)

def fetch_all_films_info():
    films_info = []  # Crée une liste vide pour stocker les informations sur les films
    base_url = "https://swapi.dev/api/films/"

    # Parcourt les 6 films dans l'API SWAPI
    for i in range(1, 7):
        url = base_url + str(i) + "/"
        data = fetch_swapi_data(url)
        # Crée un dictionnaire avec les informations du film actuel et l'ajoute à la liste
        film_info = {
            'title': data['title'],
            'episode_id': data['episode_id'],
            'director': data['director'],
            'release_date': data['release_date']
        }
        films_info.append(film_info)  # Ajoute le dictionnaire des informations du film à la liste

    return films_info  # Retourne la liste de dictionnaires des informations sur les films

# Appeler la fonction pour récupérer toutes les informations sur les films
films_info = fetch_all_films_info()

# Afficher la liste de dictionnaires de films
print(films_info)
