from django.contrib import admin
from django.urls import path
from .views import index


urlpatterns = [
    #Direct to main page in tempaltes/index.html
    path('', index, name='homepage'),

]
