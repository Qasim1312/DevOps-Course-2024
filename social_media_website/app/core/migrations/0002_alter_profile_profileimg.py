# Generated by Django 5.0.1 on 2024-01-26 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='profile-icon.png', upload_to='profile_images'),
        ),
    ]
