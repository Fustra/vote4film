from django.db import models


class Film(models.Model):
    UNIVERSAL = "U"
    PARENTAL_GUIDANCE = "PG"
    AGE_12 = "12"  # Including 12A
    AGE_15 = "15"
    AGE_18 = "18"  # Including R18
    AGE_RATING_CHOICES = [
        (UNIVERSAL, "Universal (4+)"),
        (PARENTAL_GUIDANCE, "Parental Guidance (8+)"),
        (AGE_12, "12+"),
        (AGE_15, "15+"),
        (AGE_18, "18+"),
    ]

    imdb = models.URLField(help_text="Link to the IMDB page")
    year = models.PositiveIntegerField(help_text="Year of Release")
    age_rating = models.CharField(max_length=3, choices=AGE_RATING_CHOICES)
    imdb_rating = models.FloatField(help_text="Rating on IMDB")
    trailer = models.URLField(null=True, blank=True, help_text="Link to a trailer")
    is_available = models.BooleanField(default=False, help_text="Do we have it?")
    is_watched = models.BooleanField(default=False, help_text="Have we watched it?")
