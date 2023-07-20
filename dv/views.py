from rest_framework import generics, permissions
from .models import VoiceSample, Speech
from .serializers import VoiceSampleSerializer, SpeechSerializer
from .tasks import text_to_speech_task

class VoiceSampleListCreateView(generics.ListCreateAPIView):
    serializer_class = VoiceSampleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return VoiceSample.objects.filter(user=user)

class VoiceSampleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VoiceSampleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return VoiceSample.objects.filter(user=user)
    
class SpeechListCreateView(generics.ListCreateAPIView):
    serializer_class = SpeechSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        text_to_speech_task.delay(instance.id)

    def get_queryset(self):
        user = self.request.user
        return Speech.objects.filter(user=user)
    
class SpeechRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SpeechSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Speech.objects.filter(user=user)