from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Device, DeviceInUsed, Reports
from .serializers import DeviceSerializer, DeviceInUsedSerializer
from home_cntrl.models import House
# Create your views here.


class DeviceView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class DeviceInUsedView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = DeviceInUsedSerializer
    queryset = DeviceInUsed.objects.all()

