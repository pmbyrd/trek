console.log('movies.js loaded');

const $moviesContainer = $(".movies")
let $movieCard = $(".movie-card")
const $moviesList = $(".movies-list")



async function getMovies() {
    try {
        //this call is to my own backend
        const res = await axios.get('/api/movies')
        const movies = res.data
        const titles = movies.map(movie => movie.title)
        return titles
    } catch (error) {
        console.log(error)
    }
}




async function displayMovies() {
    console.debug('displayMovies');
    try {
        let movies = await getMovies();
        //map over each movie and create a card for each movie
        // $moviesContainer.empty();
        for (let movieTitle of movies) {
            let movieData = await getMovie(movieTitle)
            $movieCard = $(`
            <div class="card" style="width: 18rem;">
                <img src="${movieData.poster}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${movieData.title}</h5>
                    <p class="card-text">${movieData.plot}</p>
                    <p class="card-text">${movieData.genre}</p>
                    <p class="card-text">${movieData.director}</p>
                    <p class="card-text">${movieData.released}</p>
                    <p class="card-text">${movieData.runtime}</p>
                    <p class="card-text">${movieData.metascore}</p>
                    <a href="/media/movie/${movieData.title}" class="btn btn-primary">${movieData.title}</a>
                </div>
            </div>
            `)
            $(".movies-list").append($movieCard)
        }       
    } catch (error) {
        console.log(error)
    }
    
}



$(document).ready(displayMovies())
// displayMovies()



