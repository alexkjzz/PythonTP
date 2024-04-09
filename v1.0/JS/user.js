const films = [
    {
        id: 1,
        titre: "Star Wars: Episode I",
    },
    {
        id: 2,
        titre: "Star Wars: Episode II",
    },
    {
        id: 3,
        titre: "Star Wars: Episode III",
    },
    {
        id: 4,
        titre: "Star Wars: Episode IV",
    },
    {
        id: 5,
        titre: "Star Wars: Episode V",
    },
    {
        id: 6,
        titre: "Star Wars: Episode VI",
    },
    {
        id: 7,
        titre: "Star Wars: Episode VII",
    },
    {
        id: 8,
        titre: "Star Wars: Episode VIII",
    },
    {
        id: 9,
        titre: "Star Wars: Episode IX",
    }
];

function creerListeFilms(){

    const listeFilms = document.getElementById("liste-films");

    films.forEach(film =>{
        const carteFilm = document.createElement("div");
        carteFilm.classList.add("carte-film");
        carteFilm.id = "film-"+ film.id;

        // Create the film title element
        const titre = document.createElement("h2");
        titre.textContent = film.titre;

        // Append the title to the film card
        carteFilm.appendChild(titre);

        // Add click event listener to the film card
        carteFilm.addEventListener('click', function () {
            toggleFavorite(carteFilm);
        });

        // Append the film card to the films list
        listeFilms.appendChild(carteFilm);
    })
}

function toggleFavorite(filmCard) {
    if (!filmCard.classList.contains('favorited')) {
        filmCard.classList.add('favorited');
    } else {
        filmCard.classList.remove('favorited');
    }
}

window.onload = creerListeFilms;



function favoris(){
    const boutonFavoris = document.createElement('button');
    boutonFavoris.innerHTML = '<i class="fa fa-heart"></i>';
    boutonFavoris.classList.add('bouton-favoris');

    return boutonFavoris;
}
