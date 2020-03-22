from operator import itemgetter

import factory
import factory.fuzzy

from films import models


class FilmFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Film

    _AGE_RATING_CHOICES = map(itemgetter(0), models.Film.AGE_RATING_CHOICES)

    imdb = factory.Sequence(lambda n: "https://example.com/film/%s" % n)
    title = factory.Sequence(lambda n: "Film #%s" % n)
    year = factory.fuzzy.FuzzyInteger(1980, 2020)
    imdb_age = factory.fuzzy.FuzzyChoice(_AGE_RATING_CHOICES)
    imdb_rating = factory.fuzzy.FuzzyFloat(1, 9)
