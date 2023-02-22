# Generated by Django 3.2.16 on 2023-02-21 19:41

import catalog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AddField(
            model_name='item',
            name='is_published',
            field=models.BooleanField(
                default=True, verbose_name='опубликовано'
            ),
        ),
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(
                default='роскошно',
                help_text='Описание должно содержать слова "роскошно" и "превосходно"',
                validators=[catalog.models.ValidateMustContain],
                verbose_name='описание',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.TextField(
                help_text='Опишите объект. Максимум 150 символов',
                validators=[django.core.validators.MaxLengthValidator(150)],
                verbose_name='название',
            ),
        ),
    ]
