# Generated by Django 4.2b1 on 2023-03-22 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0004_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='watchList',
            new_name='watchlist',
        ),
    ]
