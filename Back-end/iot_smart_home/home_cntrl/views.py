from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .models import House
from .serializers import HouseSerializer, HouseManagementSerializer
from accounts.models import Customer
from device_cntrl.models import DeviceInUsed
# Create your views here.


class Dashboard(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = HouseSerializer

    def get_queryset(self):
        user = self.request.user
        cust = Customer.objects.get(user=user)
        queryset = House.objects.filter(owner=cust).union(House.objects.filter(members__user__username__contains=user))
        return queryset


class HomeManagement(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = HouseManagementSerializer

    def get_queryset(self):
        # data = self.request.data
        id = 1
        print('hi')
        queryset = DeviceInUsed.objects.filter(device__deviceinused__house_id=id)
        return queryset
