# Generated by Django 2.2.6 on 2019-11-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Film",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imdb", models.URLField(help_text="Link to the IMDB page")),
                ("title", models.CharField(max_length=255)),
                ("year", models.PositiveIntegerField(help_text="Year of Release")),
                (
                    "age_rating",
                    models.CharField(
                        choices=[
                            ("U", "Universal (4+)"),
                            ("PG", "Parental Guidance (8+)"),
                            ("12", "12+"),
                            ("15", "15+"),
                            ("18", "18+"),
                        ],
                        max_length=3,
                    ),
                ),
                ("imdb_rating", models.FloatField(help_text="Rating on IMDB")),
                (
                    "trailer",
                    models.URLField(
                        blank=True, help_text="Link to a trailer", null=True
                    ),
                ),
                (
                    "is_available",
                    models.BooleanField(default=False, help_text="Do we have it?"),
                ),
                (
                    "is_watched",
                    models.BooleanField(default=False, help_text="Have we watched it?"),
                ),
            ],
        ),
    ]
