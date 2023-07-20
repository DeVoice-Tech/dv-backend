from django.urls import path
import dv.views as views

urlpatterns = [
    path('voice_sample/', views.VoiceSampleListCreateView.as_view(), name='voice-sample-list-create'),
    path('voice_sample/<int:pk>/', views.VoiceSampleRetrieveUpdateDestroyView.as_view(), name='voice-sample-retrieve-update-destroy'),
    path('speech/', views.SpeechListCreateView.as_view(), name='speech-list-create'),
    path('speech/<int:pk>/', views.SpeechRetrieveUpdateDestroyView.as_view(), name='speech-retrieve-update-destroy'),
]