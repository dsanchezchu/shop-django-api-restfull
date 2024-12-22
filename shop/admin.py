from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','price','category','is_active')
    list_filter = ('category','is_active')
    search_fields = ('name','description')