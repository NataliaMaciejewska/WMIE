# Generated by Django 5.1.2 on 2025-02-17 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Departments", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Department",
            new_name="Departments",
        ),
    ]
