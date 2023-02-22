# Generated by Django 3.2.16 on 2023-02-22 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20230221_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='123', help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('slug', models.SlugField(default='123', help_text='Только slug-значения, максимум 200 символов', max_length=200, unique=True, verbose_name='slug')),
                ('weight', models.PositiveSmallIntegerField(default=100, help_text='Максимум 32767', verbose_name='вес')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='123', help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('slug', models.SlugField(default='123', help_text='Только slug-значения, максимум 200 символов', max_length=200, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'тег',
                'verbose_name_plural': 'теги',
            },
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(help_text='Опишите объект. Максимум 150 символов', max_length=150, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.ForeignKey(default=True, help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория'),
        ),
        migrations.AddField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(default=True, to='catalog.Tag', verbose_name='тег'),
        ),
    ]
