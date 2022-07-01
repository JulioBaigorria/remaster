from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from . import serializers
from .permissions import ClientPermission
from .models import Client


class ClientViewSet(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    queryset = Client.objects.all()
    serializer_class = serializers.ClientListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ClientRetrieveSerializer
        if self.action == 'list':
            return serializers.ClientListSerializer
        if self.action == 'update':
            return serializers.ClientCreateOrUpdateSerializer
        elif self.action == 'create':
            return serializers.ClientCreateOrUpdateSerializer
        return self.serializer_class
