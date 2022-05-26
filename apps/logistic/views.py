from rest_framework import viewsets
from . import serializers
from .permissions import HRPermission
from .models import HR, DriverAccount, Driver, VehicleType, Vehicle, Payload


class PayloadViewSet(viewsets.ModelViewSet):
    queryset = Payload.objects.all()
    serializer_class = serializers.PayloadCreateSerializer


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = serializers.VehicleTypeCreateSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = serializers.VehicleListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.VehicleListSerializer
        if self.action == 'list':
            return serializers.VehicleListSerializer
        if self.action == 'update':
            return serializers.VehicleListSerializer
        elif self.action == 'create':
            return serializers.VehicleCreateSerializer
        return self.serializer_class


class HRViewSet(viewsets.ModelViewSet):
    permission_classes = (HRPermission,)
    queryset = HR.objects.all()
    serializer_class = serializers.HRListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.HRRetrieveSerializer
        if self.action == 'list':
            return serializers.HRListSerializer
        if self.action == 'update':
            return serializers.HRUpdateSerializer
        elif self.action == 'create':
            return serializers.HRCreateSerializer
        return self.serializer_class


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = serializers.DriverRetrieveSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.DriverRetrieveSerializer
        if self.action == 'list':
            return serializers.DriverListSerializer
        if self.action == 'update':
            return serializers.DriverUpdateSerializer
        elif self.action == 'create':
            return serializers.DriverCreateSerializer
        return self.serializer_class


class DriverAccountViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DriverAccountCreateSerializer
    queryset = DriverAccount.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.DriverAccountRetrieveSerializer
        if self.action == 'list':
            return serializers.DriverAccountListSerializer
        elif self.action == 'create':
            return serializers.DriverAccountCreateSerializer
        return self.serializer_class
