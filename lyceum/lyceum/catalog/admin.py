from django.contrib import admin

import catalog.models


class GalleryInline(admin.TabularInline):
    model = catalog.models.Gallery
    readonly_fields = ('image_tmb',)
    extra = 1


class MainImageInline(admin.TabularInline):
    model = catalog.models.MainImage
    readonly_fields = ('image_tmb',)


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
        'small_image_tmb',
    )
    list_editable = ("is_published", "text")
    list_display_links = (
        "id",
        "name",
    )
    filter_horizontal = ("tags",)
    inlines = [
        MainImageInline,
        GalleryInline,
    ]

    def category_name(self, obj):
        return obj.category.name

    category_name.short_description = 'категория'

    def small_image_tmb(self, obj):
        if obj.mainimage:
            return obj.mainimage.small_image_tmb()
        return 'Нет изображения'

    small_image_tmb.short_description = 'главное изображение'


@admin.register(catalog.models.MainImage)
class MainImageAdmin(admin.ModelAdmin):
    list_display = ('small_image_tmb', 'item_name')


@admin.register(catalog.models.Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('small_image_tmb', 'item_name')
