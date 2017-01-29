# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 18:10
from __future__ import unicode_literals

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0011_auto_20161231_1552'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('deleted', models.BooleanField(default=False, editable=False)),
                ('require_auth', models.BooleanField(default=False, verbose_name='require auth')),
                ('name', models.CharField(max_length=100)),
                ('admin_comment', models.CharField(blank=True, max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('can_edit_groups', models.ManyToManyField(blank=True, related_name='can_edit_company', to='users.AbakusGroup')),
                ('can_edit_users', models.ManyToManyField(blank=True, related_name='can_edit_company', to=settings.AUTH_USER_MODEL)),
                ('can_view_groups', models.ManyToManyField(blank=True, related_name='can_view_company', to='users.AbakusGroup')),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_created', to=settings.AUTH_USER_MODEL)),
                ('previous_contacts', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('student_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('deleted', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('mail', models.EmailField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_contacts', to='companies.Company')),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companycontact_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companycontact_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'default_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='SemesterStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('deleted', models.BooleanField(default=False, editable=False)),
                ('year', models.PositiveSmallIntegerField()),
                ('semester', models.PositiveSmallIntegerField(choices=[(0, 'Vår'), (1, 'Høst')], default=0)),
                ('contacted_status', models.PositiveSmallIntegerField(choices=[(0, 'Bedpres'), (1, 'Bedpres & Kurs'), (2, 'Kurs'), (3, 'Interessert, ikke tilbudt'), (4, 'Ikke interessert'), (5, 'Kontaktet'), (6, 'Ikke kontaktet')], default=6)),
                ('contract', models.CharField(blank=True, max_length=500)),
                ('bedex', models.BooleanField(default=False)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semester_statuses', to='companies.Company')),
                ('created_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterstatus_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='semesterstatus_updated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='semesterstatus',
            unique_together=set([('year', 'semester', 'company')]),
        ),
    ]