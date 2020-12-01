from django.contrib import admin
from .models import Product, Category, Colour

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'friendly_name',
    ]
admin.site.register(Category,CategoryAdmin)

class ColourAdmin(admin.ModelAdmin):
    list_display = [
            'colour',
            'hex_value',
        ]
admin.site.register(Colour, ColourAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'category',
        'brand_name',
        'product_name',
        'featured',
        'price',
        'image_url',
    ]
    list_editable = ['price', 'image_url', 'featured']
    list_per_page = 20

admin.site.register(Product, ProductAdmin)