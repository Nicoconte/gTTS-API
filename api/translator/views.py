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

            #response = HttpResponse(file_object, content_type="audio/mpeg")
            #response['Content-Disposition'] = 'attachment; filename="%s"' % file_name
            response = FileResponse(file_object, filename=file_name)

            return response

        else:
            return JsonResponse({"error" : "An error occurred during convertion"}, status=status.HTTP_400_BAD_REQUEST)   


    def get(self, request):
        file_name = request.query_params['name']

        if self.storage.exists(file_name):
            file_object = self.storage.open(file_name, mode="rb")

            response = HttpResponse(file_object, content_type="audio/mpeg")
            response['Content-Disposition'] = 'attachment; filename=%s' % file_name

            return response

        else:
            return JsonResponse({"error" : "Resource doesnt exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, name):
        file_name = name #request.query_params['name']    
        print(file_name)

        if self.storage.exists(file_name):
            self.storage.delete(file_name)

            return JsonResponse({"msg" : "The resource was removed from storage"}, status=status.HTTP_200_OK)
        
        else:
            return JsonResponse({"error" : "Resource doesnt exist"}, status=status.HTTP_404_NOT_FOUND)            



class TextToSpeechUrlView(APIView):
    utils = Utils()

    storage = FileSystemStorage(location=settings.MEDIA_URL)

    def post(self, request):
        print(request.body)
        body_decoded = json.loads(request.body)
        print(body_decoded)

        file_created, file_name = self.utils.translate(body_decoded, settings.MEDIA_ROOT)
        
        if file_created:            
            url = self.storage.url(file_name)

            return JsonResponse({"audio_url" : url, "name" : file_name}, status=status.HTTP_200_OK)

        else:
            return JsonResponse({"error" : "An error occurred during convertion"}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        file_name = request.query_params['name']

        self.storage = FileSystemStorage(location=settings.MEDIA_ROOT)

        if self.storage.exists(file_name):

            self.storage = FileSystemStorage(location=settings.MEDIA_URL)
            url = self.storage.url(file_name)

            return JsonResponse({"audio_url" : url}, status=status.HTTP_200_OK)

        else:
            return JsonResponse({"error" : "Resource doesnt exist"}, status=status.HTTP_404_NOT_FOUND)

    
    def delete(self, request, name):
        file_name = name #request.query_params['name']    
        print(file_name)

        self.storage = FileSystemStorage(location=settings.MEDIA_ROOT)

        if self.storage.exists(file_name):
            self.storage.delete(file_name)

            return JsonResponse({"msg" : "The resource was removed from storage"}, status=status.HTTP_200_OK)
        
        else:
            return JsonResponse({"error" : "Resource doesnt exist"}, status=status.HTTP_404_NOT_FOUND)            


