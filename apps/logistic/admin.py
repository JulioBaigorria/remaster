from django.contrib import admin
from .models import Driver, Vehicle, VehicleType, HR,DriverAccount, DriverAccountMovement
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(HR)
admin.site.register(DriverAccount)
admin.site.register(DriverAccountMovement)

# Register your models here.
