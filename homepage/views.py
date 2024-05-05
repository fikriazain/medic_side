from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import User
#unpack json
import json
# from .models import Users
# Create your views here.

def index(request):
    #get all user_id and message
    if request.session.get('user_id') is not None:
        user = User.objects.get(username=request.session.get('user_id'))
        return render(request, 'homepage.html', {'user': user})
    return render(request, 'homepage.html', {'user': None})

@csrf_exempt
def login(request):
    if request.method == 'POST':
        #get json from request
        username = request.POST['username']
        password = request.POST['password']
        #check if user exist
        user = User.objects.get(username=username)

        if user is not None:
            request.session['user_id'] = user.username
            return redirect('homepage')
        else:
            return redirect('login')

    return render(request, 'login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        name = request.POST['name']
        TTL = request.POST['ttl']

        new_user = User.objects.create_user(username=username, password=password, name=name, TTL=TTL)

        new_user.save()
        return redirect('login')

    return render(request, 'register.html')

def profile(request):
    user = User.objects.get(username=request.session.get('user_id'))
    return render(request, 'profile.html', {'user': user})

@csrf_exempt
def edit_profile(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.session.get('user_id'))
        user.blood_pressure = request.POST['blood_pressure']
        user.weight = request.POST['weight']
        user.vein = request.POST['vein']
        user.temp = request.POST['temp']
        user.drink_perday = request.POST['drink_perday']
        user.food = request.POST['food']
        user.save()
        return redirect('profile')
    return render(request, 'edit-profile.html')

def logout(request):
    request.session['user_id'] = None
    return redirect('homepage')

