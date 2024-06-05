import json
from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from deep_translator import GoogleTranslator
import datetime
import zoneinfo



# Create your views here.
@csrf_exempt
def first_message(request):
    jakarta_tz = zoneinfo.ZoneInfo('Asia/Jakarta')
    jakarta_time = datetime.datetime.now(jakarta_tz)
    data ={
        'username': request.session.get('user_id'),
        "current_date_time": jakarta_time.strftime("%Y-%m-%d %I:%M:%S %p %A"),
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://127.0.0.1:5006/first_message', json=data, headers=headers)
    return JsonResponse(response.json())

@csrf_exempt
def index(request):
    return render(request, 'index_chat.html')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        text = json.loads(request.body)['input']
        translated_text = GoogleTranslator(source='id', target='english').translate(text)
        response = get_llm_response(translated_text, request.session.get('user_id'))
        response['response'] = GoogleTranslator(source='english', target='id').translate(response['response'])
        return JsonResponse(response)

@csrf_exempt
def get_llm_response(text, username):
    data = {'input': text, 'username': username}
    headers = {'Content-Type': 'application/json'}
    try:
        print("Fetching LLM response...")
        response = requests.post('http://127.0.0.1:5006/query', json=data, headers=headers)
        response_json = response.json()
        return response_json            
    except Exception as e:
        print(f"Error fetching LLM response: {e}")
        return "Error: Failed to fetch response from LLM server"