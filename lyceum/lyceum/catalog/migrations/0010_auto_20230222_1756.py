# Generated by Django 3.2.16 on 2023-02-22 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0009_auto_20230222_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(
                default=[0],
                help_text='Выберите категорию',
                on_delete=django.db.models.deletion.CASCADE,
                to='catalog.category',
                verbose_name='категория',
            ),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(
                default=[0], to='catalog.Tag', verbose_name='тег'
            ),
        ),
    ]
