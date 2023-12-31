# Generated by Django 4.2.2 on 2023-08-16 11:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("staffs", "0011_remove_staff_role"),
        ("corecode", "0014_assignment_delete_assignments"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseMaterial",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "file",
                    models.FileField(blank=True, null=True, upload_to="assignments"),
                ),
                (
                    "date_created",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "due_date",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, null=True
                    ),
                ),
                ("total_marks", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "academic_semester",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.academicsemester",
                    ),
                ),
                (
                    "academic_session",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.academicsession",
                    ),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corecode.course",
                    ),
                ),
                (
                    "lecturer",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="lecturer_assignment",
                        to="staffs.staff",
                    ),
                ),
            ],
            options={
                "ordering": ["-date_created"],
            },
        ),
        migrations.DeleteModel(
            name="Assignment",
        ),
    ]
