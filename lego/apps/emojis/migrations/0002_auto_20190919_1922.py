# Generated by Django 2.1.7 on 2019-09-19 19:22

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import lego.apps.files.models


class Migration(migrations.Migration):

    dependencies = [
        ("files", "0003_auto_20171210_1610"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("emojis", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "deleted",
                    models.BooleanField(db_index=True, default=False, editable=False),
                ),
                ("name", models.CharField(max_length=40, unique=True)),
                ("unicode_string", models.CharField(max_length=24)),
                (
                    "created_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="category_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "updated_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="category_updated",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="emoji", old_name="disabled", new_name="approved"
        ),
        migrations.AddField(
            model_name="emoji",
            name="image",
            field=lego.apps.files.models.FileField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="emoji_image",
                to="files.File",
            ),
        ),
        migrations.AlterField(
            model_name="emoji",
            name="fitzpatrick_scale",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="emoji",
            name="unicode_string",
            field=models.CharField(db_index=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name="emoji",
            name="category_link",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="emojis",
                to="emojis.Category",
            ),
        ),
    ]
