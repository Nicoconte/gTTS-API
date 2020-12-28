from django.urls import path

from .views import TextToSpeechBlobView, TextToSpeechUrlView

urlpatterns = [
    path('text-to-speech/blob/', TextToSpeechBlobView.as_view()), #post
    path('text-to-speech/blob/<str:name>/', TextToSpeechBlobView.as_view()),
    path('text-to-speech/blob/?<str:name>/', TextToSpeechBlobView.as_view()), #get
    
    path('text-to-speech/url/', TextToSpeechUrlView.as_view()), #post 
    path('text-to-speech/url/<str:name>/', TextToSpeechUrlView.as_view()),
    path('text-to-speech/url/?<str:name>/', TextToSpeechUrlView.as_view()), #get

] 
