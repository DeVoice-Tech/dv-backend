from rest_framework import serializers
from .models import VoiceSample, Speech, Tone

class VoiceSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceSample
        fields = ['id', 'wav', 'parent']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class SpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech
        fields = ['id', 'user', 'text', 'emotion', 'status', 'wav']
        read_only_fields = ['user', 'status', 'wav']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

