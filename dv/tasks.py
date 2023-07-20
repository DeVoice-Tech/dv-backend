from celery import shared_task
from .models import Speech

@shared_task
def text_to_speech_task(speech_id):
    speech = Speech.objects.get(pk=speech_id)

    # TODO: implement text to speech
