from django.db import models


class IsPublishedBaseModel(models.Model):
    is_published = models.BooleanField(
        "опубликовано",
        default=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class SlugBaseModel(models.Model):
    slug = models.SlugField(
        "slug",
        max_length=200,
        unique=True,
        help_text="Только slug-значения, максимум 200 символов",
    )

    class Meta:
        abstract = True


class UniqueNameBaseModel(models.Model):
    name = models.CharField(
        "название",
        max_length=150,
        unique=True,
        help_text="Максимум 150 символов",
    )

    class Meta:
        abstract = True
