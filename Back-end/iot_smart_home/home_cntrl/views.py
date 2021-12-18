from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from .models import House
from .serializers import HouseSerializer
from accounts.models import Customer
# Create your views here.


class Dashboard(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = HouseSerializer

    def get_queryset(self):
        user = self.request.user
        cust = Customer.objects.get(user=user)
        queryset = House.objects.filter(owner=cust).union(House.objects.filter(members__user__username__contains=user))
        return queryset





