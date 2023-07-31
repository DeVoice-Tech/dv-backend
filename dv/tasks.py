from celery import shared_task
import logging
from celery import Task
from tortoise.api import TextToSpeech

from .models import Speech
from .services import text_to_speech
from .apps import DvConfig

class TTSTask(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.
    """
    abstract = True

    def __init__(self):
        super().__init__()
        self.model = None

    def __call__(self, *args, **kwargs):
        """
        Load model on first call
        """
        if not self.model:
            logging.info("Tortoise-TTS is loading...")
            self.model = TextToSpeech(use_deepspeed=True, half=True, kv_cache=True)
            logging.info("Tortoise-TTS has loaded...")
            
        return self.run(*args, **kwargs)

@shared_task(
    bind=True,
    base=TTSTask
)
def text_to_speech_task(cls, speech_id):
    speech = Speech.objects.get(pk=speech_id)

    text_to_speech(
        tortoise_instance=cls.model,
        text=speech.text,
        emotion=speech.emotion,
        voice_dirs=[
            speech.user.voice_samples.filter(parent='F').first().wav.path,
            speech.user.voice_samples.filter(parent='M').first().wav.path,
        ],
        results_dir=speech.wav.path
    )

    speech.status = speech.StatusChoices.COMPLETE
    speech.save()