from django.urls import path

from votes import views

app_name = "votes"
urlpatterns = [
    path("create/", views.VoteCreate.as_view(), name="vote-create"),
    path("", views.VoteAggregate.as_view(), name="vote-aggregate"),
]
