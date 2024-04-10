
import requests
def fetch_films():
    response = requests.get('https://swapi.dev/api/films/')
    if response.status_code == 200:
        films_data = response.json()['results']
        filtered_films = [{'title': film['title'], 'episode_id': film['episode_id'], 'director': film['director']} for film in films_data]
        return filtered_films
    else:
        print('Erreur lors de la récupération des données des films:', response.status_code)
        return None

data = (fetch_films())
print(data)