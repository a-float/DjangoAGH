# Generated by Django 3.0.5 on 2020-04-30 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Movie',
        ),
    ]
