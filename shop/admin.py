from django.contrib import admin
from .models import Product, Make, CarListing

# Register your models here.
class CarListingAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

admin.site.register(CarListing, CarListingAdmin)

class MakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

admin.site.register(Make)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['mileage', 'price', 'stock', 'year_made', 'description', 'image']


admin.site.register(Product, ProductAdmin)
