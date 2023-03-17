# Generated by Django 3.2.16 on 2023-03-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('feedback', '0002_feedback_status_processing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='status_processing',
            field=models.TextField(
                choices=[
                    ('received', 'получено'),
                    ('in processing', 'в обработке'),
                    ('ancwer is given', 'ответ дан'),
                ],
                default='получено',
                verbose_name='статус обработки',
            ),
        ),
    ]
