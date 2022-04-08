from abc import ABC

from rest_framework import serializers
from .models import HR


class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = '__all__'



