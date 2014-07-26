from django.contrib import admin
from keys.models import Product, SKU, Key

class KeyAdmin(admin.ModelAdmin):
	fields = ['key', 'sku', 'key_type', 'allocated_to', 'allocated_by', 'allocated_at', 'imported_at']

class SKUAdmin(admin.ModelAdmin):
	fields = ['name', 'product']

class ProductAdmin(admin.ModelAdmin):
	fields = ['name']
  

admin.site.register(Key, KeyAdmin)
admin.site.register(SKU, SKUAdmin)
admin.site.register(Product, ProductAdmin)
