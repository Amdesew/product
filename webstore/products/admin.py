from django.contrib import admin
from products.models import Products

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Products, ProductsAdmin)