import json
from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from deep_translator import GoogleTranslator



# Create your views here.
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
        response = requests.post('http://127.0.0.1:5005/query', json=data, headers=headers)
        response_json = response.json()
        return response_json
    except Exception as e:
        print(f"Error fetching LLM response: {e}")
        return "Error: Failed to fetch response from LLM server"