# Generated by Django 2.2.6 on 2019-10-17 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='author',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='by',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='wish',
        ),
    ]
