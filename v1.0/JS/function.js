
var jsdata = JSON.parse('{{ json_data | safe }}');
console.log(jsdata)



function creerListeFilms(){

    const listeFilms = document.getElementById("liste-films");

    films.forEach(film =>{
        const carteFilm = document.createElement("div");
        carteFilm.classList.add("carte-film")
        carteFilm.id = "film-"+ film.id;

        const title = document.createElement("h2");
        title.textContent = film.title;

        const statistique = document.createElement("p");
        statistique.textContent = film.statistique;

        carteFilm.appendChild(title);
        carteFilm.appendChild(statistique);
        listeFilms.appendChild(carteFilm);
    })
}

window.onload = creerListeFilms;