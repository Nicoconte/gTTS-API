from django.urls import path

from .views import TextToSpeechBlobView, TextToSpeechUrlView, TextToSpeechView


urlpatterns = [
    path('text-to-speech/blob/', TextToSpeechBlobView.as_view()),
    path('text-to-speech/url/', TextToSpeechUrlView.as_view()),
    path('text-to-speech/', TextToSpeechView.as_view())
]
