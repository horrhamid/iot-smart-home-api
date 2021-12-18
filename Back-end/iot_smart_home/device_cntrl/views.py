from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Device
from .serializers import DeviceSerializer
from home_cntrl.models import House
# Create your views here.


class Dashboard(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = DeviceSerializer

    # def get_queryset(self, id):
    #     id = self.request.POST.get('id')
    #     cust = Device.objects.filter(id=id)
    #     queryset = House.objects.filter(owner=cust).union(House.objects.filter(members__user__username__contains=user))
    #     return queryset