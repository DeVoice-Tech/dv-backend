from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import DVUserSerializer

class DVUserTokenObtainPairSerializer(TokenObtainPairSerializer):
    user_serializer_class = DVUserSerializer

    def validate(self, attrs):
        data = super().validate(attrs)
        
        user = self.user_serializer_class(self.user).data
        data['user'] = user
        
        return data
