# Generated by Django 2.2.6 on 2019-11-02 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0004_film_poster_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="film",
            name="genre",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
