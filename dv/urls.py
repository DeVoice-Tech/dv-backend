from django.urls import path
from .views import VoiceSampleListCreateView, VoiceSampleRetrieveUpdateDestroyView

urlpatterns = [
    path('voice_sample/', VoiceSampleListCreateView.as_view(), name='voice-sample-list-create'),
    path('voice_sample/<int:pk>/', VoiceSampleRetrieveUpdateDestroyView.as_view(), name='voice-sample-retrieve-update-destroy'),
]