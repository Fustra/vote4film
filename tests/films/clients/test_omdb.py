import json
from pathlib import Path

import pytest
import responses

from films.clients import omdb
from films.core import types


@responses.activate
def test_get_film():
    INPUT_URL = "https://www.imdb.com/title/tt1853728/"
    MOCK_URL = "http://www.omdbapi.com/?apikey=&i=tt1853728"
    responses.add(
        responses.GET,
        MOCK_URL,
        json=json.loads((Path(__file__).parent / "omdb_tt1853728.json").read_text()),
    )

    result = omdb.get_film("", INPUT_URL)

    assert result == types.Film(
        imdb=INPUT_URL,
        title="Django Unchained",
        year=2012,
        imdb_age=types.AgeRating.AGE_18,
        imdb_rating=8.4,
        genre="Drama, Western",
        runtime_mins=165,
        plot=(
            "With the help of a German bounty hunter, a freed slave sets out to "
            "rescue his wife from a brutal Mississippi plantation owner."
        ),
        poster_url="https://m.media-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_SX300.jpg",
    )


@pytest.mark.parametrize(
    "input, expected",
    [
        ("Not Rated", None),
        ("N/A", None),
        ("G", types.AgeRating.UNIVERSAL),
        ("PG", types.AgeRating.PARENTAL_GUIDANCE),
        ("PG-13", types.AgeRating.AGE_12),
        ("TV-MA", types.AgeRating.AGE_18),
        ("R", types.AgeRating.AGE_18),
    ],
)
def test_age_rating(input, expected):
    assert omdb._age_rating(input) == expected
