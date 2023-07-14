# Generated by Django 4.2.2 on 2023-07-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("corecode", "0008_course_code_course_credit_unit_course_lecturer_and_more"),
        ("students", "0004_rename_registration_number_student_mat_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="courses",
            field=models.ManyToManyField(related_name="students", to="corecode.course"),
        ),
        migrations.AlterField(
            model_name="student",
            name="current_status",
            field=models.CharField(
                choices=[("active", "Active"), ("graduate", "Graduate ")],
                default="active",
                max_length=10,
            ),
        ),
    ]