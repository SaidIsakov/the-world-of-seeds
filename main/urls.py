from django.urls import path
from .views import*

urlpatterns = [
    path('', index, name='index' ),
    path('products/<slug:slug>/', product_detail, name='product_detail'),
    path('categories', get_categories, name='get_categories'),
    path('subcategories/<slug:slug>/', get_subcategories, name='get_subcategories'),
    path('product/<slug:slug>/', get_products_list, name='get_products_list')
]
