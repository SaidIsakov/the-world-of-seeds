from django.urls import path
from .views import*


 
urlpatterns = [
    path('create_order/', create_order, name='create_order'),
    path('order_succsess/', order_success, name='order_success')
]