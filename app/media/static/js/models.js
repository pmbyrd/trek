console.log("hello from inside the models.js file");
const OMDBAPI = "http://www.omdbapi.com/?i=tt3896198&apikey=";

async function getAPIKey() {
	console.debug("getAPIKey");
	try {
		const res = await axios.get("/api/OMDB_API_KEY");
		const API_KEY = res.data;
		return API_KEY;
	} catch (error) {
		console.error(error);
	}
}



async function getMovie(movieTitle) {
	console.debug("getMovie");
	try {
		const API_KEY = await getAPIKey();
		const res = await axios.get(`${OMDBAPI}${API_KEY}&t=${movieTitle}`);
		let movie = res.data;
		return (movie = {
			title: movie.Title,
			year: movie.Year,
			rated: movie.Rated,
			released: movie.Released,
			runtime: movie.Runtime,
			genre: movie.Genre,
			director: movie.Director,
			metascore: movie.Metascore,
			imdbRating: movie.imdbRating,
			plot: movie.Plot,
			poster: movie.Poster,
			genre: movie.Genre,
			actors: movie.Actors,
			imdbID: movie.imdbID,
		});
	} catch (error) {
		console.log(error);
	}
}

async function getActors(title) {
	console.debug("getActors");
	try {
        
	} catch (error) {
        console.error(error);
    }
}
