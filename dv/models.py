from __future__ import annotations
from django.db import models

import dv.utils as utils

class VoiceSample(models.Model):
    """
    A model to save the tone voice samples.
    """
    class ParentChoices(models.TextChoices):
        FATHER = 'F', 'Father'
        MOTHER = 'M', 'Mother'
    
    user = models.ForeignKey('dv_users.DVUser', on_delete=models.CASCADE)
    tone = models.ForeignKey('Tone', on_delete=models.CASCADE, null=True, blank=True)
    wav = models.FileField(upload_to=utils.voice_samples_directory_path)
    parent = models.CharField(max_length=1, choices=ParentChoices.choices)

    def __str__(self):
        return self.wav.name

class Speech(models.Model):
    """
    A model to temporarily store the outputted speech.
    """
    class StatusChoices(models.TextChoices):
        PENDING = 'P', 'Pending'
        COMPLETE = 'C', 'Complete'
        
    user = models.ForeignKey('dv_users.DVUser', on_delete=models.CASCADE)
    text = models.TextField()
    status = models.CharField(
        max_length=1, 
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    wav = models.FileField(upload_to=utils.speech_directory_path)

    def __str__(self):
        return self.text

class Tone(models.Model):
    """
    A model to store the tone weights for a user.
    """
    user = models.ForeignKey('dv_users.DVUser', on_delete=models.CASCADE)
    weights = models.FileField(upload_to=utils.tones_directory_path)
