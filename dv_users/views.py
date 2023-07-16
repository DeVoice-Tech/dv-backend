from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .tokens import DVUserTokenObtainPairSerializer
from .models import DVUser
from .serializers import DVUserSerializer
class DVUserTokenObtainPairView(TokenObtainPairView):
    serializer_class = DVUserTokenObtainPairSerializer

class DVUserListCreateView(generics.ListCreateAPIView):
    queryset = DVUser.objects.all()
    serializer_class = DVUserSerializer

class DVUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DVUser.objects.all()
    serializer_class = DVUserSerializer