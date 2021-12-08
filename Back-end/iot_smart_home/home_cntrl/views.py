from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import House
from accounts.models import Customer
# Create your views here.


class Dashboard(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        user = request.user
        cust = Customer.objects.get(user=user)
        h = House.objects.filter(owner=cust)
        print(h)
        return Response(200 * 5)





