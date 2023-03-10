# Generated by Django 4.1.4 on 2022-12-17 05:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('college_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staffs',
            name='profile_img',
            field=models.ImageField(blank=True, default='Profile-img/user-default.png', null=True, upload_to='Profile-img/'),
        ),
        migrations.AddField(
            model_name='students',
            name='profile_img',
            field=models.ImageField(blank=True, default='Profile-img/std-image.png', null=True, upload_to='Profile-img/'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
