from django.contrib import admin
from .models import products

class Admin(admin.ModelAdmin):
    search_fields=['Name', 'Description']
    list_display=['Name', 'Price', 'Release_date']
    list_editable=['Price']
    list_filter=['Price']


admin.site.register(products, Admin)