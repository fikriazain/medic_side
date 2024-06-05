from django.urls import path
from .views import index, send_message, first_message  # Import the view for chatting with LLM

urlpatterns = [
    # Direct to main page in templates/index.html
    path('', index, name='index_message'),
    path('send_message/', send_message, name='send_message'),  # Add the URL for chatting with LLM
    path('first_message/', first_message, name='first_message'),
]