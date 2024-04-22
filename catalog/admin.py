from django.contrib import admin
from django.contrib.auth.models import Group

from catalog.models import Category, Product
from django.contrib.auth.models import User


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


class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('permissions',)


admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
