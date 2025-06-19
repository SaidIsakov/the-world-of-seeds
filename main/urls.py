from django.urls import path
from .views import*

urlpatterns = [
    path('', index, name='index' ),
    path('products/<slug:slug>/', product_detail, name='product_detail'),
    path('catalog', get_categories, name='get_categories')
    
]