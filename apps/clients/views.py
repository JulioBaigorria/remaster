from rest_framework import viewsets
from . import serializers
from .permissions import ClientPermission
from .models import Client

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (ClientPermission,)
    queryset = Client.objects.all()
    serializer_class = serializers.ClientListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.ClientRetrieveSerializer
        if self.action == 'list':
            return serializers.VehicleListSerializer
        if self.action == 'update':
            return serializers.ClientCreateOrUpdateSerializer
        elif self.action == 'create':
            return serializers.ClientCreateOrUpdateSerializer
        return self.serializer_class