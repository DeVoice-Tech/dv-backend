from rest_framework import generics, permissions
from .models import VoiceSample
from .serializers import VoiceSampleSerializer

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