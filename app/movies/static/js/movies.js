console.log('movies.js loaded');
const API_KEY = "4cc3d718d79609d7b538246e87a080f0"
const Base_URL = 'https://api.themoviedb.org/'
const $moviesContainer = $(".movies")

const OMDBAPI = "http://www.omdbapi.com/?i=tt3896198&apikey=cbdaf169"



async function getMovies() {
    try {
        //this call is to my own backend
        const res = await axios.get('/movies/get_movies')
        const titles = res.data.movies.map(movie => movie.title)
        return titles
    } catch (error) {
        console.log(error)
    }
}


async function getMovie(movieTitle) {
    try {
        const res = await axios.get(`${OMDBAPI}&t=${movieTitle}`);
        const movie = res.data
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






displayMovies()