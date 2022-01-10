from rest_framework import serializers

from .models import House
from device_cntrl.models import DeviceInUsed


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = '__all__'


class HouseManagementSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = DeviceInUsed
        fields = '__all__'
