import pytest
from django.db import IntegrityError

from factories import FilmFactory
from films.models import Film


@pytest.mark.django_db
def test_FilmCreate_DUPLICATE_ERROR_TEXT():
    FilmFactory.create(title="title", year=2000)

    with pytest.raises(IntegrityError) as err:
        FilmFactory.create(title="title", year=2000)

    assert err.value.args[0] == Film.DUPLICATE_ERROR_TEXT
