from django.contrib import admin
from .models import Category, Product, Gallery, Subcategory, DescriptionImage
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Gallery)

admin.site.register(DescriptionImage)