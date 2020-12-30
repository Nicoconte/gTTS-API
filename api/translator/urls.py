from django.urls import path

from .views import TextToSpeechBlobView

urlpatterns = [
    path('text-to-speech/blob/', TextToSpeechBlobView.as_view()), #post
] 
