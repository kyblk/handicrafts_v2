from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import MainSlider, Catalog, ProductImage, Product


# Register your models here.

@admin.register(MainSlider)
class MainSliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'image', 'is_visible')


@admin.register(Catalog)
class CatalogAdmin(DraggableMPTTAdmin):
    fields = ('label', 'image')


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    fields = ('image', 'priority')
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('catalog', 'label', 'price', 'description', 'is_visible')
    list_display = ('label', 'catalog', 'price', 'is_visible')
    search_fields = ['label']
    inlines = [ProductImageInline, ]
