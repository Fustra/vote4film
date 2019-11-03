from django.conf import settings
from django.db import models

from films.models import Film


class VoteQuerySet(models.QuerySet):
    def next_film_to_vote(self, user):
        return (
            Film.objects.exclude(is_watched=True)
            .exclude(pk__in=Vote.objects.filter(user=user).values_list("film"))
            .first()
        )


class Vote(models.Model):
    class Meta:
        unique_together = [["user", "film"]]

    YES = 2
    YES_MAYBE = 1
    NO = -1
    NO_SEEN_IT = -2
    AGE_RATING_CHOICES = [
        (YES, "Yes please"),
        (YES_MAYBE, "Yes - if I must"),
        (NO, "No thanks"),
        (NO_SEEN_IT, "No - already seen it"),
    ]

    objects = VoteQuerySet.as_manager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    film = models.ForeignKey("films.Film", on_delete=models.CASCADE)
    choice = models.IntegerField(choices=AGE_RATING_CHOICES)

    def __str__(self):
        return f"Vote by {self.user} of {self.choice} for {self.film}"

    def __repr__(self):
        return f"<Vote(pk={self.pk})>"
