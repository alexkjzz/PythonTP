

var k = "" //variable du nombre de favoris qui sera determiné par l'id "i" des films..
const films = [
    {
        id: 1,
        titre: "Star Wars: Episode I",
        statistique: "Nombre de favoris: " + k,
    },
    {
        id: 2,
        titre: "Star Wars: Episode II",
        statistique: "Nombre de favoris: " + k,
    },
    {
        id: 3,
        titre: "Star Wars: Episode III",
        statistique: "Nombre de favoris: " + k,
    },
    {
        id: 4,
        titre: "Star Wars: Episode IV",
        statistique: "Nombre de favoris: " + k,
    },
    {
        id: 5,
        titre: "Star Wars: Episode V",
        statistique: "Nombre de favoris: " + k,
    },
    {
        id: 6,
        titre: "Star Wars: Episode VI",
        statistique: "Nombre de favoris: " + k,
    },
    {
        id: 7,
        titre: "Star Wars: Episode VII",
        statistique: "Nombre de favoris: " + k,
    },
    {
        id: 8,
        titre: "Star Wars: Episode VIII",
        statistique: "Nombre de favoris: " + k,
    },
    {
        id: 9,
        titre: "Star Wars: Episode IX",
        statistique: "Nombre de favoris: " + k,
    }
];

function creerListeFilms(){

    const listeFilms = document.getElementById("liste-films");

    films.forEach(film =>{
        const carteFilm = document.createElement("div");
        carteFilm.classList.add("carte-film")
        carteFilm.id = "film-"+ film.id;

        const titre = document.createElement("h2");
        titre.textContent = film.titre;

        const statistique = document.createElement("p");
        statistique.textContent = film.statistique;

        carteFilm.appendChild(titre);
        carteFilm.appendChild(statistique);

        listeFilms.appendChild(carteFilm);
    })
}

window.onload = creerListeFilms;