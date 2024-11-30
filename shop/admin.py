from django.contrib import admin
from .models import Product, Make

# Register your models here.

class MakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

admin.site.register(Make)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['mileage', 'price', 'stock', 'year_made', 'description', 'image']


admin.site.register(Product, ProductAdmin)
