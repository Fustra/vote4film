# Generated by Django 2.2.6 on 2019-11-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("votes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vote",
            name="choice",
            field=models.IntegerField(
                choices=[
                    (2, "Yes please"),
                    (1, "Yes - if I must"),
                    (-1, "No thanks"),
                    (-2, "No - definitely not"),
                ]
            ),
        ),
    ]
