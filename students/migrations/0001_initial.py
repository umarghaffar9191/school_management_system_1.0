# Generated by Django 5.1 on 2024-08-11 22:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("gender", models.CharField(max_length=30)),
                ("date_of_birth", models.DateField()),
                ("addmission_no", models.IntegerField(unique=True)),
                ("addmission_date", models.DateField()),
                ("address", models.CharField(default="Optional", max_length=200)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone_number", models.CharField(max_length=20)),
                ("emergency_contact_phone", models.CharField(max_length=20)),
                (
                    "current_class",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
            ],
        ),
    ]
