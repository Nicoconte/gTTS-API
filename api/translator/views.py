from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, HttpResponse
from django.conf import settings

from rest_framework.views import APIView
from rest_framework import status

from .utils import Utils

import json


"""
We only need post method due that heroku doesnt persistance the uploaded files. Heroku´s filesystem is ephemeral 
For more information: https://help.heroku.com/K1PPS2WM/why-are-my-file-uploads-missing-deleted 
"""
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
            return response

        else:
            return JsonResponse({"error" : "An error occurred during convertion"}, status=status.HTTP_400_BAD_REQUEST)   


