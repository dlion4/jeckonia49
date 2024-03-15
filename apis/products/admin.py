from django.contrib import admin

# Register your models here.
from .models import ProductVariant, Product

class ProductVariantInlines(admin.StackedInline):
    model = ProductVariant
    extra = 0
    prepopulated_fields = {"slug": ("sku", "name")}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'variants']
    inlines = [
        ProductVariantInlines
    ]
