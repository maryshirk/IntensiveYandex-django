# Generated by Django 3.2.16 on 2023-02-22 14:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0006_auto_20230222_1659'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
