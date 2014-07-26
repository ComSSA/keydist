from django.contrib import admin
from keys.models import Product, SKU, Key

class KeyAdmin(admin.ModelAdmin):
	list_display = ['key', 'sku', 'key_type', 'allocated_to', 'allocated_by', 'allocated_at', 'imported_at']

class SKUAdmin(admin.ModelAdmin):
	list_display = ['name', 'product']

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name']
  

admin.site.register(Key, KeyAdmin)
admin.site.register(SKU, SKUAdmin)
admin.site.register(Product, ProductAdmin)
