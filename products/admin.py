from django.contrib import admin
from .models import MainProducts, SpecialSale, NewProducts

# Customizing the Information being displayed in the Admin Page


class MainProducstAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Stock')


class NewProductsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Price', 'Stock')


class SaleDiscountsAdmin(admin.ModelAdmin):
    list_display = ('CouponCode', 'Description', 'Discount')


# Register your models here.
admin.site.register(MainProducts, MainProducstAdmin)
admin.site.register(NewProducts, NewProductsAdmin)
admin.site.register(SpecialSale, SaleDiscountsAdmin)
