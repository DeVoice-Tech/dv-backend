from rest_framework_simplejwt.views import TokenObtainPairView
from .tokens import DVUserTokenObtainPairSerializer

class DVUserTokenObtainPairView(TokenObtainPairView):
    serializer_class = DVUserTokenObtainPairSerializer
