# Generated by Django 3.2.23 on 2023-12-15 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20231211_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_lz2hfc', upload_to='images/'),
        ),
    ]