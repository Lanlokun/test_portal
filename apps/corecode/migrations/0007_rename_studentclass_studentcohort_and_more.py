# Generated by Django 4.2.2 on 2023-06-20 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_auto_20201124_0614"),
        ("finance", "0002_alter_invoice_options_and_more"),
        ("result", "0004_rename_current_class_result_current_cohort"),
        ("corecode", "0006_rename_academicterm_academicsemester"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="StudentClass",
            new_name="StudentCohort",
        ),
        migrations.AlterModelOptions(
            name="studentcohort",
            options={
                "ordering": ["name"],
                "verbose_name": "Cohort",
                "verbose_name_plural": "Cohorts",
            },
        ),
    ]