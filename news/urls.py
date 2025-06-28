from django.urls import path
from .views import*


urlpatterns = [
    path('news/', News, name='news' ),
]