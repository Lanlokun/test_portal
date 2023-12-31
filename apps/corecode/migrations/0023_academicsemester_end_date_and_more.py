# Generated by Django 4.2.2 on 2023-10-06 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0022_alter_studentcourse_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="academicsemester",
            name="end_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="academicsemester",
            name="start_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="academicsession",
            name="end_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="academicsession",
            name="start_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
