from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name', 'category_description')
    search_fields = ('category_name', 'category_description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'product_cost', 'product_category',)
    list_filter = ('product_category', 'product_is_publicated')
    search_fields = ('product_name', 'product_description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'version_product', 'version_name', 'version_number', 'version_is_active',)
    list_filter = ('version_is_active',)
    search_fields = ('version_name',)
