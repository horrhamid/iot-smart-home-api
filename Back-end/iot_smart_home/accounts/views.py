from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Contractor, Customer
from .serializers import UserSerializer, ContractorSerializer, CustomerSerializer


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={'message': f'Bye {request.user.username}!'},
            status=status.HTTP_204_NO_CONTENT
        )


class UserRegistration(generics.CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CustomerRegistration(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data.copy()
        data.update({"user": request.user})
        print(data)
        customer_ser = CustomerSerializer(data=data)
        if customer_ser.is_valid():
            customer_ser.save(user=request.user)
            return Response("customer_ser", 201)

        return Response(customer_ser.errors, 400)


class ContractorRegistration(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data.copy()
        data.update({"user": request.user})
        print(data)
        contractor_ser = ContractorSerializer(data=data)
        if contractor_ser.is_valid():
            contractor_ser.save(user=request.user)
            return Response("contractor_ser", 201)

        return Response(contractor_ser.errors, 400)
