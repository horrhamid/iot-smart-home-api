
from rest_framework import serializers

from .models import Device, DeviceInUsed, Reports


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceInUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInUsed
        fields = '__all__'



class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'