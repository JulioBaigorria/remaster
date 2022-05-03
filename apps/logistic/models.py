from django.db import models
from django.db.models.signals import post_save, pre_save
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
    name = models.CharField('Vehicle Name', max_length=65, blank=True, )
    axes_quantity = models.IntegerField('Axes quantity', default=0, blank=True)
    type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, )
    domain = models.CharField('Domain', max_length=20, null=True, default=None, )
    desc = models.CharField(max_length=65, default='', unique=False, blank=True)

    class Meta:
        abstract = True


class Vehicle(CommonVehicle):
    """Vehicle Class Model"""
    fuel_type = models.ForeignKey(FuelType, on_delete=models.CASCADE, blank=True, null=True)
    last_odom = models.FloatField('Las odometer calculation', default=0, blank=True)

    def __str__(self):
        return f'{self.name}'


class Payload(CommonVehicle):
    """Payload Class Model"""
    max_load = models.FloatField("Max Load in Kgs", max_length=300000)

    def __str__(self):
        return f'{self.name}'


class Driver(models.Model):
    """Driver Class Model from User Model"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle', blank=True, null=True)
    payload = models.ForeignKey(Payload, on_delete=models.CASCADE, related_name='payload', blank=True, null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.user}'


class HR(models.Model):
    """HR Class Model"""
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='driver', null=True)
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE, related_name='hr_vehicle',
                                blank=True, default=None)
    payload = models.ForeignKey(Payload, null=True, on_delete=models.CASCADE, related_name='hr_payload',
                                blank=True, default=None)

    start_date = models.DateTimeField(auto_now_add=True)
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


class DriverAccountMovement(models.Model):
    debit = models.FloatField(max_length=50000, blank=True, null=True)
    credit = models.FloatField(max_length=50000, blank=True, null=True)
    total = models.FloatField(max_length=50000, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.driver}'s movement"


class DriverAccount(models.Model):
    driver = models.OneToOneField(Driver,
                                  on_delete=models.CASCADE, related_name='account')
    movements = models.ForeignKey(DriverAccountMovement, on_delete=models.CASCADE, related_name='movements', blank=True,
                                  null=True)
    total = 50000

    class Meta:
        ordering = ['driver']

    def __str__(self):
        return f"{self.driver}'s movement"

    def get_total_balance(self):
        total_balance = DriverAccountMovement.objects.filt


def add_first_movement(sender, instance, **kwargs):
    first_mov = DriverAccountMovement.objects.create(debit=50000, credit=0, total=50000, driver=instance.driver)
    first_mov.save()

# def get_end_odom():
#     query = HR.objects.filter(driver=44).all()
#     print(len(query))


# post_save.connect(add_first_movement, sender=DriverAccount)
post_save.connect(add_first_movement, sender=DriverAccount)
