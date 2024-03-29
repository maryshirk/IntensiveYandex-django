# Generated by Django 3.2.16 on 2023-03-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        default='',
                        help_text='Максимум 150 символов',
                        max_length=150,
                        verbose_name='имя',
                    ),
                ),
                (
                    'mail',
                    models.EmailField(
                        default='1@example.com',
                        help_text='Максимум 254 символа',
                        max_length=254,
                        verbose_name='почта',
                    ),
                ),
                ('text', models.TextField(verbose_name='фидбэк')),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='дата написания'
                    ),
                ),
            ],
            options={
                'verbose_name': 'фидбэк',
                'verbose_name_plural': 'фидбэки',
            },
        ),
    ]
