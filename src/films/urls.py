from django.urls import path

from films import views

app_name = "films"
urlpatterns = [
    path("create/", views.FilmCreate.as_view(), name="film-create"),
    path("<int:pk>/", views.FilmUpdate.as_view(), name="film-update"),
]
