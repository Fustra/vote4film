import requests

from films.core import types


def get_film(api_key, url: str) -> types.Film:
    if not url.startswith("https://www.imdb.com/title/"):
        raise ValueError("Must be a direct link to a specific IMDB film")

    imdb_id = url[len("https://www.imdb.com/title/") :].partition("/")[0]

    response = requests.get(f"http://www.omdbapi.com/?apikey={api_key}&i={imdb_id}")
    response.raise_for_status()
    json = response.json()

    title = json["Title"]
    year = int(json["Year"])
    age_rating = types.AgeRating(json["Rated"].replace("R", "18"))
    imdb_rating = float(json["imdbRating"])
    runtime_mins = None
    if "min" in json["Runtime"]:
        runtime_mins = int(json["Runtime"].split()[0])
    plot = json["Plot"]
    poster_url = json["Poster"]

    return types.Film(
        imdb=url,
        title=title,
        year=year,
        age_rating=age_rating,
        imdb_rating=imdb_rating,
        runtime_mins=runtime_mins,
        plot=plot,
        poster_url=poster_url,
    )
