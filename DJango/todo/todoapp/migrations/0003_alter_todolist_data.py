# Generated by Django 4.2.6 on 2023-12-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0002_rename_todolis_todolist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todolist",
            name="data",
            field=models.CharField(max_length=40),
        ),
    ]
