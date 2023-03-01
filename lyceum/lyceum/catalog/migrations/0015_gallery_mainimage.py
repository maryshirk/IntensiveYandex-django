# Generated by Django 3.2.16 on 2023-02-28 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0014_alter_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainImage',
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
                    'image',
                    models.ImageField(
                        upload_to='previews/%Y/%m/%d',
                        verbose_name='главное изображение товара',
                    ),
                ),
                (
                    'item',
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='catalog.item',
                        verbose_name='товар',
                    ),
                ),
            ],
            options={
                'verbose_name': 'главное изображение',
                'verbose_name_plural': 'главные изображения',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
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
                    'image',
                    models.ImageField(
                        upload_to='previews/%Y/%m/%d',
                        verbose_name='главное изображение товара',
                    ),
                ),
                (
                    'item',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='catalog.item',
                        verbose_name='товар',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Фото товара',
                'verbose_name_plural': 'Фотогалерея товара',
            },
        ),
    ]
