# genai_webapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('upload-code/', views.upload_code, name='upload_code'),   # Route for uploading code
    path('upload-quiz/', views.upload_quiz, name='upload_quiz'),   # Route for uploading quiz
    path('chat/', views.chat_view, name='chat_view'),      # New interactive chat page
    path('result-chat/', views.result_chat_view, name='result_chat'), # Chat result page
]
