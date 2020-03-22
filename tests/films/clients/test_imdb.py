from pathlib import Path

import responses

from films.clients import imdb
from films.core import types


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
        imdb_age=types.AgeRating.AGE_18,
        imdb_rating=8.4,
    )
