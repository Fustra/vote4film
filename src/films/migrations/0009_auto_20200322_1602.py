# Generated by Django 2.2.11 on 2020-03-22 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0008_film_bbfc_age"),
    ]

    operations = [
        migrations.RenameField(
            model_name="film",
            old_name="age_rating",
            new_name="imdb_age",
        ),
    ]
