# Generated by Django 4.1.3 on 2022-11-26 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_newsletter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsletter',
        ),
    ]