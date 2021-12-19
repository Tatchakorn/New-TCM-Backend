from django.db import models
from rest_framework import serializers
from .models import Pulse


class PulseSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format=r"%a, %d %b %Y %H:%M:%S %Z")
    data = serializers.JSONField()
    class Meta:
        model = Pulse
        fields = ('name', 'data', 'time', 'remarks',)