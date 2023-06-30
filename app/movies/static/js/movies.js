console.log('movies.js loaded');
const API_KEY = "4cc3d718d79609d7b538246e87a080f0"
const Base_URL = 'https://api.themoviedb.org/'

async function getMovies() {
    try {
        //this call is to my own backend
        const res = await axios.get('/movies')
        console.log(res.data)
    } catch (error) {
        console.log(error)
    }
}

getMovies()

async function getMovie(movie) {
    try {
        const res = await axios.get(`https://api.themoviedb.org/3/search/movie?query=${movie}&api_key=4cc3d718d79609d7b538246e87a080f0`)
        console.table(res.data.results)
    } catch (error) {
        console.log(error)
    }
}

getMovie("star trek")