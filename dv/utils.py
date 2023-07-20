from django.utils import timezone

def voice_samples_directory_path(instance, filename):
    # Get the username of the associated user
    username = instance.user.username

    # Get the parent
    parent = instance.parent

    # Append the current timestamp to the filename to make it unique
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename = f"{filename}_{timestamp}"

    # Return the upload path
    return f"voice_samples/{username}/{parent}/{filename}"

def speech_directory_path(instance, filename):
    # Get the username of the associated user
    username = instance.user.username

    # Append the current timestamp to the filename to make it unique
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename = f"{filename}_{timestamp}"

    # Return the upload path
    return f"speech/{username}/{filename}"

def tones_directory_path(instance, filename):
    # Get the username of the associated user
    username = instance.user.username

    # Append the current timestamp to the filename to make it unique
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename = f"{filename}_{timestamp}"

    # Return the upload path
    return f"tones/{username}/{filename}"
