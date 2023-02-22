from catalog.validators import ValidateMustContain

from core.models import IsPublishedMixin, SlugMixin, UniqueNameMixin

from django.db import models


class Category(UniqueNameMixin, IsPublishedMixin, SlugMixin):
    weight = models.PositiveSmallIntegerField(
        "вес",
        default=100,
        help_text="Максимум 32767",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name[:15]


class Tag(UniqueNameMixin, IsPublishedMixin, SlugMixin):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name[:15]


class Item(
    UniqueNameMixin,
    IsPublishedMixin,
):
    text = models.TextField(
        "описание",
        help_text="Описание должно содержать слова 'роскошно' и 'превосходно'",
        validators=[
            ValidateMustContain("превосходно", "роскошно"),
        ],
        default="роскошно",
    )

    category = models.ForeignKey(
        "Category",
        verbose_name="категория",
        on_delete=models.CASCADE,
        help_text="Выберите категорию",
        default=[0],
    )
    tags = models.ManyToManyField(
        "Tag",
        verbose_name="тег",
        default=[0],
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name[:15]
