from django.apps import AppConfig
from tortoise.api import TextToSpeech


class DvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dv'
    
    # load the model when the application starts (singleton)
    # NOTE: TORTOISE_MODELS_DIR should be set in the environment
    # with the path to the downloaded models. Otherwise, the
    # default models will be DOWNLOADED (shit's huge).
    tortoise_tts = TextToSpeech(use_deepspeed=True, half=True, kv_cache=True)
