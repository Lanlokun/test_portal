# Generated by Django 4.2.2 on 2023-09-12 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0017_alter_coursematerial_due_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="academicsemester",
            name="session",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="corecode.academicsession",
            ),
        ),
    ]
