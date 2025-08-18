from django.urls import path
from .views import*


 
urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('order_success/', order_success, name='order_success')
]