# Generated by Django 4.2.2 on 2023-08-10 02:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0010_alter_studentcourse_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentcourse",
            name="registration_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]