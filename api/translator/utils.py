from django.core.files.storage import FileSystemStorage
from django.conf import settings

from gtts import gTTS

import uuid

class Utils:

    storage = FileSystemStorage(location=settings.MEDIA_ROOT)

    """
    Summary: Get the entry text and convert it into a mp3 file. 
    Return: Boolean. True if the file was created successfully. Otherwise, return False
            String. File name
    Params: Dictionary with the information
    """
    def translate(self, params, path):

        if 'text' not in params or 'language' not in params or 'should_be_slow' not in params:
            return False #Bad request

        text = params['text']
        language = params['language']
        slow = params['should_be_slow']

        file_name = f"{uuid.uuid4()}.mp3"
        final_path = path

        translator = gTTS(text=text, lang=language, slow=slow)
        translator.save(f"{final_path}{file_name}")        
        
        return self.storage.exists(file_name), file_name



