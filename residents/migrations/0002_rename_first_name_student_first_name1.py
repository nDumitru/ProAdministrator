# Generated by Django 4.1.4 on 2023-01-07 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("residents", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="residents",
            old_name="first_name",
            new_name="first_name1",
        ),
    ]
