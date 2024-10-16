from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('message/', include('message.urls')),
    path('chat/', include('chat.urls')),
]
