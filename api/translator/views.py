from gtts_api.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, FileResponse, HttpResponse
from django.conf import settings

from rest_framework.views import APIView
from rest_framework import status

from .utils import Utils

import json


class TextToSpeechBlobView(APIView):
    utils = Utils()

    storage = FileSystemStorage(location=settings.MEDIA_ROOT)

    def post(self, request):
        body_decoded = json.loads(request.body)

        file_created, file_name = self.utils.translate(body_decoded, settings.MEDIA_ROOT) 

        if file_created:
            file_object = self.storage.open(file_name, mode="rb")

            response = HttpResponse(file_object, content_type="audio/mpeg")
            response['Content-Disposition'] = 'attachment; filename="%s"' % file_name
            #response = FileResponse(file_object)

            return response

        else:
            return JsonResponse({"error" : "An error occurred during convertion"}, status=status.HTTP_400_BAD_REQUEST)   


    def get(self, request):
        body_decoded = json.loads(request.body)
        file_name = body_decoded['name'] 

        if self.storage.exists(file_name):
            file_object = self.storage.open(file_name, mode="rb")

            response = HttpResponse(file_object, content_type="audio/mpeg")
            response['Content-Disposition'] = 'attachment; filename=%s' % file_name

            return response

        else:
            return JsonResponse({"error" : "Resource doesnt exist"}, status=status.HTTP_404_NOT_FOUND)



class TextToSpeechUrlView(APIView):
    utils = Utils()

    storage = FileSystemStorage(location=settings.MEDIA_URL)

    def post(self, request):
        body_decoded = json.loads(request.body)
        file_created, file_name = self.utils.translate(body_decoded, settings.MEDIA_ROOT)
        
        if file_created:            
            url = self.storage.url(file_name)

            return JsonResponse({"audio_url" : url}, status=status.HTTP_200_OK)

        else:
            return JsonResponse({"error" : "An error occurred during convertion"}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        body_decoded = json.loads(request.body)
        file_name = body_decoded['name']

        self.storage = FileSystemStorage(location=settings.MEDIA_ROOT)

        if self.storage.exists(file_name):

            self.storage = FileSystemStorage(location=settings.MEDIA_URL)
            url = self.storage.url(file_name)

            return JsonResponse({"audio_url" : url}, status=status.HTTP_200_OK)

        else:
            return JsonResponse({"error" : "Resource doesnt exist"}, status=status.HTTP_404_NOT_FOUND)


class TextToSpeechView(APIView):

    storage = FileSystemStorage(location=MEDIA_ROOT)

    def delete(self, request):
        body_decoded = json.loads(request.body)
        file_name = body_decoded['name']

        if self.storage.exists(file_name):
            self.storage.delete(file_name)

            return JsonResponse({"msg" : "The resource was removed from storage"}, status=status.HTTP_200_OK)
        
        else:
            return JsonResponse({"error" : "Resource doesnt exist"}, status=status.HTTP_404_NOT_FOUND)