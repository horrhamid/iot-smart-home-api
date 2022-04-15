from rest_framework import serializers
from .models import Update


class HomeUpdateStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Update
        fields = '__all__'