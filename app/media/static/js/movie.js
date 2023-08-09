console.log("hello from inside the movie.js file")
let movieTitle = $(".movie-title").text()

async function displayMovie(movieTitle) {
    console.debug("displayMovie");
    try {
        let movie = await getMovie(movieTitle);
        $movieCard = $(`
            <div class="card" style="width: 18rem;">
                <img src="${movie.poster}" class="card-img-top" alt="...">
                <div class="card-body">
                <h5 class="card-title">${movie.title}</h5>
                <p class="card-text">${movie.plot}</p>
                `)
        $(".movie-card").append($movieCard)
    } catch (error) {
        console.error(error);
    }
}

$(document).ready(displayMovie(movieTitle))