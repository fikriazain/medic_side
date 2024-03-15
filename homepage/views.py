from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
#unpack json
import json
# from .models import Users
# Create your views here.

def index(request):
    #get all user_id and message
    print(request.session.get('user_id'))
    return render(request, 'homepage.html')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        #get json from request
        username = request.POST['username']
        password = request.POST['password']
        #Put session in user_id
        request.session['user_id'] = username

    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        new_user = User.objects.create_user(username=username, password=password)
        new_user.save()

    return render(request, 'register.html')

