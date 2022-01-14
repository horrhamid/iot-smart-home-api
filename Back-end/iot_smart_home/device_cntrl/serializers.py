
from rest_framework import serializers

from .models import Device, DeviceInUsed


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceInUsedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceInUsed
        fields = '__all__'
