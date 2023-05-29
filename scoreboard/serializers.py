from rest_framework import serializers
from .models import ScoreBoard

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreBoard
        fields = '__all__'