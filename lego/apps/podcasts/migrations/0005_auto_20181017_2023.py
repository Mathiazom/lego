# Generated by Django 2.0.6 on 2018-10-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podcasts', '0004_remove_podcast_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='source',
            field=models.CharField(max_length=500),
        ),
    ]