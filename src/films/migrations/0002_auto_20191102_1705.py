# Generated by Django 2.2.6 on 2019-11-02 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("films", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="film", unique_together={("title", "year")},
        ),
    ]