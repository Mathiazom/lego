# Generated by Django 3.0.14 on 2021-11-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0007_meeting_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="mazemap_poi",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
