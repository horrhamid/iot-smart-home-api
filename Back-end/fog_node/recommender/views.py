from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .serializers import ReportsSerializer
from accounts.models import Customer
from .models import Reports


class RecommenderView(viewsets.ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = ReportsSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        try:
            customer = Customer.objects.get(user__id=user_id)
            device_type = request.query_params.get('type')
            queryset = Reports.objects.filter(customer=customer, device__device__type=device_type)
            print('queryset: ', queryset)
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"Status": 'customer does not exists', 'status_code': status.HTTP_404_NOT_FOUND})
