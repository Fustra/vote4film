from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from film.clients import imdb
from film.models import Film


class FilmList(ListView):
    model = Film


class FilmCreate(CreateView):
    model = Film
    fields = ["imdb", "is_available"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        film = imdb.get_film(self.object.imdb)
        self.object.title = film.title
        self.object.year = film.year
        self.object.age_rating = film.age_rating.value
        self.object.imdb_rating = film.imdb_rating
        return super().form_valid(form)


class FilmUpdate(UpdateView):
    model = Film
    fields = [
        "imdb",
        "year",
        "age_rating",
        "imdb_rating",
        "trailer",
        "is_available",
        "is_watched",
    ]
