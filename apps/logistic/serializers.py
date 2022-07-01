from django.contrib.auth.models import Group
from rest_framework import serializers
from .models import HR, DriverAccount, Driver, Vehicle, VehicleType, Payload


class PayloadCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payload
        fields = ('name', 'type', 'domain', 'max_load')


class VehicleTypeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('name',)


class VehicleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('name', 'type', 'domain',)


class VehicleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'


'''
-Create the HR Class and its attributes.
-When a new HR is created, it has to take the end_odom and end_city of the previous HR.
-If is the first HR, it have to return 0 on start_odom and "sauce viejo" on start_city.
-The user can create another HR if the actual is not already closed.

'''


class HRCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = ('driver',)

    def create(self, validated_data):
        try:
            last_hr = HR.objects.filter(driver=validated_data['driver']).all()
        except ValueError:
            print("Not Found")
        if len(last_hr) > 0:
            last_hr_obj = last_hr[::-1]
            if last_hr_obj[0].end_odom == 0 or \
                    last_hr_obj[0].load_city is None or \
                    last_hr_obj[0].download_city is None or \
                    last_hr_obj[0].end_city is None or \
                    last_hr_obj[0].end_date is None:

                raise serializers.ValidationError(
                    {"error": "Can't create a new HR. Make sure you ended the previous one"})
            else:
                vehicle = Vehicle.objects.filter(id=validated_data['driver'].vehicle.id)
                payload = Payload.objects.filter(id=validated_data['driver'].payload.id)
                new_hr = HR(driver=validated_data['driver'])
                new_hr.start_city = last_hr_obj[0].end_city
                new_hr.start_odom = last_hr_obj[0].end_odom
                new_hr.vehicle_id = vehicle[0].id
                new_hr.payload_id = payload[0].id
                print(new_hr.__dict__)
                new_hr.save()
                return new_hr

        else:
            vehicle = Vehicle.objects.filter(id=validated_data['driver'].vehicle.id)
            payload = Payload.objects.filter(id=validated_data['driver'].payload.id)
            new_hr = HR(driver=validated_data['driver'])
            new_hr.start_city = "Sauce Viejo"
            new_hr.start_odom = 0
            new_hr.vehicle_id = vehicle[0].id
            new_hr.payload_id = payload[0].id
            print(new_hr.__dict__)
            new_hr.save()
            return new_hr


class HRUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = ('start_date', 'end_date', 'end_odom', 'load_city', 'download_city',
                  'end_city', 'vehicle', 'payload',)


class HRListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = '__all__'


class HRRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = '__all__'


class HRDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = ('id',)


class DriverRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class DriverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('id', 'user', 'vehicle', 'payload',)


class DriverCreateSerializer(serializers.ModelSerializer):
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
        return value


class DriverUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ('vehicle', 'payload')


class DriverAccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAccount
        fields = ('driver',)

    def validate_owner(self, value):
        try:
            driver_account = DriverAccount.objects.filter(owner=value.id)[:1].get()
            print(driver_account)
        except DriverAccount.DoesNotExist:
            pass


class DriverAccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAccount
        fields = ('owner', 'total')


class DriverAccountRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverAccount
        fields = ('owner', 'movements', 'total')
