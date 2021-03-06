from django.contrib import admin
from django.utils.safestring import mark_safe
from shop.forms import ColorModelAdminForms
from .models import ProductModel, productTagModel, CategoryModel, BrandModel, ColorModel, SizeModel
from .models import *


@admin.register(productTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['created_at']

@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['created_at']

@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'color']
    list_display_links = ['code']
    search_fields = ['code']
    list_filter = ['created_at']
    form = ColorModelAdminForms

    def color(self, obj):
        free_spice = '&nbsp;' * 2
        return mark_safe(f"<div style='background-color:{obj.code}; width: 20px;'>{free_spice}</div>")



@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['created_at']



@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'real_price', 'discount', 'created_at', 'sale']
    list_display_links = ['title', 'price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'price']
    autocomplete_fields = ['category', 'tags', 'sizes', 'colors']
    readonly_fields = ['real_price', 'sale']
