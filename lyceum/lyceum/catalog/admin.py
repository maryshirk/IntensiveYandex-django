import catalog.models

from django.contrib import admin


@admin.register(catalog.models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ("name", "slug", "is_published", "weight")
    list_display = ("name", "is_published")
    list_editable = ("is_published",)


@admin.register(catalog.models.Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ("name", "slug", "is_published")
    list_display = ("name", "is_published")
    list_editable = ("is_published",)


@admin.register(catalog.models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        catalog.models.Item.name.field.name,
        "text",
        "is_published",
    )
    list_editable = ("is_published", "text")
    list_display_links = ("id", "name",)
    filter_horizontal = ("tags",)
