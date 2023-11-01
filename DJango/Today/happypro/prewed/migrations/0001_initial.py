# Generated by Django 4.2.6 on 2023-11-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=30)),
                ("Number", models.IntegerField()),
                ("Address", models.IntegerField()),
            ],
            options={
                "db_table": "prewed",
            },
        ),
    ]