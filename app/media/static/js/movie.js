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

async function displayCast(movieTitle) {
    console.debug("displayCast");
    try {
        const cast = await getCast(movieTitle);
        console.log(cast);
        
        for (let actor of cast) {
            let $actorCard = $(`
                <div class="card" style="width: 18rem;">
                    <img src="${actor.profile_path}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">${actor.character}</h5>
                        <p>
                            <a href="/media/performers/${actor.name}" class="btn btn-primary">${actor.name}</a>
                        </p>
                        <p class="card-text">${actor.name}</p>
                    </div>
                </div>
            `);
            
            $(".cast-list").append($actorCard);
            
            // I only want to append the first 10 actors
        }
    } catch (error) {
        console.error(error);
    }
}

$(document).ready(displayMovie(movieTitle))
$(document).ready(displayCast(movieTitle))