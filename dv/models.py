from __future__ import annotations
from django.db import models
from django.utils import timezone

def user_directory_path(instance, filename):
    # Get the username of the associated user
    username = instance.user.username

    # Append the current timestamp to the filename to make it unique
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename = f"{filename}_{timestamp}"

    # Return the upload path
    return f"voice_samples/{username}/{filename}"

class VoiceSample(models.Model):
    class ParentChoices(models.TextChoices):
        FATHER = 'F', 'Father'
        MOTHER = 'M', 'Mother'
    
    user = models.ForeignKey('dv_users.DVUser', on_delete=models.CASCADE)
    wav = models.FileField(upload_to=user_directory_path)
    parent = models.CharField(max_length=1, choices=ParentChoices.choices)

    def __str__(self):
        return self.wav.name
