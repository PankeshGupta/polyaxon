# Generated by Django 2.0.3 on 2018-04-14 07:40

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import libs.resource_validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, validators=[libs.resource_validation.validate_resource])),
                ('memory', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, validators=[libs.resource_validation.validate_resource])),
                ('gpu', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True, validators=[libs.resource_validation.validate_resource])),
            ],
        ),
    ]
