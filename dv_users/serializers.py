from rest_framework import serializers
from .models import DVUser

class DVUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DVUser
        fields = ['id', 'username', 'email', 'is_active', 'is_admin']
