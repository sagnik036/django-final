# Generated by Django 3.2 on 2022-09-14 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_teachers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]
