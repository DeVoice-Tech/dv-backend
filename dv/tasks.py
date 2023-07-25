from celery import shared_task
from .models import Speech
from .services import text_to_speech
from .apps import DvConfig

@shared_task
def text_to_speech_task(speech_id):
    speech = Speech.objects.get(pk=speech_id)

    text_to_speech(
        tortoise_instance=DvConfig.tortoise_tts,
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