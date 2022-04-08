from django.db import models
from django.conf import settings


class FuelType(models.Model):
    """Fuel Type Model"""
    name = models.CharField('Combustible Type Name', max_length=30)


class VehicleType(models.Model):
    """Vehicle Type Model"""
    name = models.CharField('Vehicle Type Name', max_length=60, unique=True)

    def __str__(self):
        return f'{self.name}'


class CommonVehicle(models.Model):
    """Common Abstract Vehicle Model"""
    name = models.CharField('Vehicle Name', max_length=65, )
    axes_quantity = models.IntegerField('Axes quantity', default=0)
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    domain = models.CharField('Domain', max_length=20, null=True, default=None)
    desc = models.CharField(max_length=65, default='', unique=False)

    class Meta:
        abstract = True


class Vehicle(CommonVehicle):
    """Vehicle Class Model"""
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE)
    last_odom = models.FloatField('Las odometer calculation', default=0)

    def __str__(self):
        return f'{self.name}'


class Payload(CommonVehicle):
    """Payload Class Model"""
    max_load = models.FloatField("Max Load in Kgs", max_length=300000)

    def __str__(self):
        return f'{self.name}'


class Driver(models.Model):
    """Driver Class Model from User Model"""
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle')
    payload = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='payload')

    def __str__(self):
        return f'{self.name}'


class HR(models.Model):
    """HR Class Model"""
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver', null=True)
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE, related_name='hr_vehicle',
                                default='vehicle')
    payload = models.ForeignKey(Payload, null=True, on_delete=models.CASCADE, related_name='hr_payload',
                                default='payload')

    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    start_odom = models.FloatField(default=0)
    end_odom = models.FloatField(default=0)

    start_city = models.CharField(max_length=50, null=True)
    load_city = models.CharField(max_length=50, null=True)
    download_city = models.CharField(max_length=50, null=True)
    end_city = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'HR Nro {self.id}'

    def count_trip_days(self):
        return self.end_date - self.start_date


class DriverAccount(models.Model):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='account')
    total_balance = models.FloatField(max_length=500000)
