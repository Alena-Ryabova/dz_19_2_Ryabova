from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ist_display = ('id', 'category_name')
    list_filter = ('category_name',)
    search_fields = ('category_name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    ist_display = ('id', 'product_name', 'purchase_price', 'category')
    list_filter = ('category',)
    search_fields = ('category', 'product_description')
