# Generated by Django 4.1.4 on 2022-12-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management_app', '0004_remove_subjects_staff_subjects_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='staff',
            field=models.ManyToManyField(blank=True, to='college_management_app.staffs'),
        ),
    ]
