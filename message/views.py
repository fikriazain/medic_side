from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
#unpack json
import json
from .models import Message
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    #get all user_id and message
    messages = Message.objects.all()
    context = {
        'messages': messages
    }
    return render(request, 'index.html', context)

@csrf_exempt
def get_message(request):
    if request.method == 'POST':
        #get json data
        data = json.loads(request.body)
        #get message
        message = data['message']
        user_id = data['user_id']
        #Store to database
        message = Message(user_id=user_id, message=message)
        message.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

@csrf_exempt
def delete_all_data(request):
    if request.method == 'POST':
        #delete all data
        try:
            Message.objects.all().delete()
        except:
            print("No data to delete")
        
        #redirect using url
        return HttpResponseRedirect('/message/')
    else:
        return render(request, 'index.html')