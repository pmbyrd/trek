console.log('movies.js loaded');
const API_KEY = "4cc3d718d79609d7b538246e87a080f0"
const Base_URL = 'https://api.themoviedb.org/'
const $moviesContainer = $(".movies")
let $movieCard = $(".movie-card")
const $moviesList = $(".movies-list")

const OMDBAPI = "http://www.omdbapi.com/?i=tt3896198&apikey=cbdaf169"



async function getMovies() {
    try {
        //this call is to my own backend
        const res = await axios.get('/api/movies')
        const movies = res.data
        const titles = movies.map(movie => movie.title)
        console.log(titles)
        return titles
    } catch (error) {
        console.log(error)
    }
}

getMovies()

async function getMovie(movieTitle) {
    try {
        const res = await axios.get(`${OMDBAPI}&t=${movieTitle}`);
        let movie = res.data
        return movie = {
            title: movie.Title,
            year: movie.Year,
            rated: movie.Rated,
            released: movie.Released,
            runtime: movie.Runtime,
            genre: movie.Genre,
            director: movie.Director,
            metascore: movie.Metascore,
            plot: movie.Plot,
            poster: movie.Poster,
        }
    } catch (error) {
        console.log(error);
    }
}

async function displayMovies() {
    console.debug('displayMovies');
    try {
        let movies = await getMovies();
        console.log(movies)
        //map over each movie and create a card for each movie
        // $moviesContainer.empty();
        for (let movieTitle of movies) {
            let movieData = await getMovie(movieTitle)
            console.log(movieData)
            $movieCard = $(`
            <div class="card" style="width: 18rem;">
                <img src="${movieData.poster}" class="card-img-top" alt="...">
                <div class="card-body">
                    <h5 class="card-title">${movieData.title}</h5>
                    <p class="card-text">${movieData.plot}</p>
                    <p class="card-text">${movieData.genre}</p>
                    <p class="card-text">${movieData.director}</p>
                    <p class="card-text">${movieData.released}</p>
                    <a href="#" class="btn btn-primary">Go somewhere</a>
                </div>
            </div>
            `)
            $moviesContainer.append($movieCard)
        }       
    } catch (error) {
        console.log(error)
    }
    
}



$(document).ready(displayMovies())
// displayMovies()



