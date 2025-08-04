from django.urls import path
from .views import*


 
urlpatterns = [
    path('create-order/', create_order, name='create-order')
]