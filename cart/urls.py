from django.urls import path
from .views import*

urlpatterns = [
    path('cart/',CartView.as_view(), name='cart'),
    path('products/add/<int:products_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:cart_id>/', cart_remove, name='cart_remove'),
    path('/change/<int:cart_id>/<str:action>/', cart_change_quantity, name='change_quantity'),
    
    
]