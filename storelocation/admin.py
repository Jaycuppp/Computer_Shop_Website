from django.contrib import admin
from .models import Store

# Customizing the Information being displayed in the Admin Page


class StoreAdmin(admin.ModelAdmin):
    list_display = ('Street', 'City', 'State', 'Zip',
                    'Phone', 'Opens', 'Closes')


# Register your models here.
admin.site.register(Store, StoreAdmin)
