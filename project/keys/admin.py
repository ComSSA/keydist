# coding=utf-8
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from .models import Product, SKU, Key


@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):

    list_display = ['key', 'sku', 'key_type', 'allocated_to', 'allocated_by',
                    'allocated_at', 'imported_at']
    search_fields = ['key']


@admin.register(SKU)
class SKUAdmin(admin.ModelAdmin):

    list_display = ['name', 'product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['name']
