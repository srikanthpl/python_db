# Generated by Django 4.2.6 on 2023-12-12 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Todolis",
            new_name="Todolist",
        ),
    ]
