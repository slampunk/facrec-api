from rest_framework import serializers
from recognition.models import RecognitionRequest


class RecognitionRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognitionRequest
        fields = ['traderId', 'image']
