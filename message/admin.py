from django.contrib import admin
from .models import Message
# Register your models here.

#Register Message model to admin site and show the PK 
admin.site.register(Message)
