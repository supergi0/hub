# Generated by Django 4.2.2 on 2023-10-06 04:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0034_tournament_positionpool_pool_crosspool_bracket_match"),
    ]

    operations = [
        migrations.AddField(
            model_name="tournament",
            name="logo_dark",
            field=models.FileField(blank=True, max_length=256, upload_to="tournament_logos/"),
        ),
        migrations.AddField(
            model_name="tournament",
            name="logo_light",
            field=models.FileField(blank=True, max_length=256, upload_to="tournament_logos/"),
        ),
    ]
