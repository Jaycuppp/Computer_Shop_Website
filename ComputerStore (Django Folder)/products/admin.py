from django.contrib import admin
from .models import Product, SpecialSale

# Customizing the Information being displayed in the Admin Page
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Stock')

class SaleDiscounts(admin.ModelAdmin):
    list_display = ('CouponCode', 'Description', 'Discount')

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(SpecialSale, SaleDiscounts)