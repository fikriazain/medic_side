from django.contrib import admin
from django.urls import path
from .views import index, login, register


urlpatterns = [
    #Direct to main page in tempaltes/index.html
    path('', index, name='homepage'),
    path('login/', login, name='login'),
    path('register/', register, name='register')


]
