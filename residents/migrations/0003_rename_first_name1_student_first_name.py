# Generated by Django 4.1.4 on 2023-01-07 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("residents", "0002_rename_first_name_student_first_name1"),
    ]

    operations = [
        migrations.RenameField(
            model_name="residents",
            old_name="first_name1",
            new_name="first_name",
        ),
    ]