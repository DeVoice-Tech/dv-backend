from __future__ import annotations
from django.db import models

from .utils import voice_samples_directory_path, tones_directory_path

class VoiceSample(models.Model):
    class ParentChoices(models.TextChoices):
        FATHER = 'F', 'Father'
        MOTHER = 'M', 'Mother'
    
    user = models.ForeignKey('dv_users.DVUser', on_delete=models.CASCADE)
    tone = models.ForeignKey('Tone', on_delete=models.CASCADE, null=True, blank=True)
    wav = models.FileField(upload_to=voice_samples_directory_path)
    parent = models.CharField(max_length=1, choices=ParentChoices.choices)

    def __str__(self):
        return self.wav.name

class Tone(models.Model):
    user = models.ForeignKey('dv_users.DVUser', on_delete=models.CASCADE)
    weights = models.FileField(upload_to=tones_directory_path)