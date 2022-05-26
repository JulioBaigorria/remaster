from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'cuit',)


class ClientRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id' ,'name', 'cuit', 'address', 'city', 'pcode', 'created_at',)

class ClientCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'cuit', 'address', 'city', 'pcode',)

'''class DriverCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('user', 'vehicle', 'payload')

    def validate_user(self, value):
        try:
            query_set = Group.objects.filter(user=value)
            if query_set[0].name != "Driver":
                raise serializers.ValidationError("Must be in the group 'Driver'")
        except Group.DoesNotExist:
            pass
        return value'''
