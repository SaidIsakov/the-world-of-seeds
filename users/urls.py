from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', login_user, name='login'),
    path('registration/',register_user, name='registration'),
    path('logout/', logout_user, name='logout')
]
