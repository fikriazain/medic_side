from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
#unpack json
import json

# Create your views here.

def index(request):
    #get all user_id and message
    return render(request, 'homepage.html')