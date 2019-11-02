from django.urls import path

from films import views

urlpatterns = [
    path("", views.FilmList.as_view(), name="film-list"),
    path("create/", views.FilmCreate.as_view(), name="film-create"),
    path("<int:pk>/", views.FilmUpdate.as_view(), name="film-update"),
]
