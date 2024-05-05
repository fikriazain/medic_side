from django.contrib import admin
from django.urls import path
from .views import index, login, register, profile, edit_profile, logout


urlpatterns = [
    #Direct to main page in tempaltes/index.html
    path('', index, name='homepage'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit_profile'),
    path('logout/', logout, name='logout')

]
