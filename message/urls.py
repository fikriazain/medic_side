from django.contrib import admin
from django.urls import path
from .views import index, get_message, delete_all_data


urlpatterns = [
    #Direct to main page in tempaltes/index.html
    path('', index, name='index_message'),
    path('get_message/', get_message, name='get_message'),
    path('delete/', delete_all_data, name='delete_all_data')

]
