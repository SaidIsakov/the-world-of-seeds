from django.contrib import admin
from .models import Category, Product, Gallery, Subcategory, DescriptionImage
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'slug')


#Продукты
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'price', 'category', 'availability')
    list_filter = ('price', 'category')
    list_editable = ('price', 'availability')


#Подкатегории
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'subcategory_category', 'is_popular_subcategory')
    list_editable = ('is_popular_subcategory',)


#Фотографии доля продуктов
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'products')
    


#Фотографии для описания
@admin.register(DescriptionImage)
class DescriptionImageAdmin(admin.ModelAdmin):
    list_display = ('decription_image', 'products')
    