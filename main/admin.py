from django.contrib import admin
from .models import Category, Product, Gallery, Subcategory, DescriptionImage
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'slug')


#Фотографии доля продуктов
class ImageInline(admin.TabularInline):
    model = Gallery
    raw_id_fields = ['products']


#Фотографии для описания
class DiscriptionImageInline(admin.TabularInline):
    model = DescriptionImage
    raw_id_fields = ['products']


#Продукты
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'price', 'category', 'availability', 'is_popular_product', 'is_hero_product')
    list_filter = ('price', 'category', 'id')
    list_editable = ('price', 'availability')
    inlines = [ImageInline, DiscriptionImageInline]


#Подкатегории
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title', 'subcategory_category', 'is_popular_subcategory')
    list_editable = ('is_popular_subcategory',)
