from pathlib import Path

import responses

from film.clients import imdb
from film.core import types


@responses.activate
def test_get_film():
    URL = "https://www.imdb.com/title/tt1853728/"
    responses.add(
        responses.GET,
        URL,
        body=(Path(__file__).parent / "tt1853728.html").read_bytes(),
    )

    result = imdb.get_film(URL)

    assert result == types.Film(
        imdb=URL,
        title="Django Unchained",
        year=2012,
        age_rating=types.AgeRating.AGE_18,
        imdb_rating=8.4,
    )
