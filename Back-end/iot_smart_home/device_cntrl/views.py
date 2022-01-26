from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Device, DeviceInUsed, Reports
from accounts.models import Customer
from home_cntrl.models import House
from .serializers import DeviceSerializer, DeviceInUsedSerializer
from home_cntrl.models import House


class DeviceView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class DeviceInUsedView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = DeviceInUsedSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        try:
            user = Customer.objects.get(user__id=user_id)
            house_id = request.query_params.get('id')
            if House.objects.filter(Q(owner__user__id=user_id) | Q(members__user__id=user_id), id=house_id):
                queryset = DeviceInUsed.objects.filter(house__id=house_id)
                print('queryset: ', queryset)
                page = self.paginate_queryset(queryset)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response(serializer.data)

                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)
        except Exception as e:
            return Response({"Status": 'house or customer does not exists', 'status_code': status.HTTP_404_NOT_FOUND})
        
    def check_user(self, user_id, house_id):
        try:
            user = Customer.objects.get(user__id=user_id)
            house = House.objects.filter(Q(owner__user__id=user_id) | Q(members__user__id=user_id), id=house_id)
            if user and house:
                return user
        except:
            pass
        return False
    
    def create(self, request, *args, **kwargs):
        customer = self.check_user(request.user.id, request.data.get('house'))
        if customer:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            Reports.objects.create(device=serializer.instance, 
                                   customer=customer,
                                   new_volume=serializer.data.get('volume'),
                                   new_state=serializer.data.get('state'))
            
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({"status": "User is not customer or User is not owner/member of the house"})

    def perform_create(self, serializer):
        serializer.save()
    
    def update(self, request, *args, **kwargs):
        customer = self.check_user(request.user.id, request.data.get('house'))

        if customer:
            partial = kwargs.pop('partial', False)
            instance = DeviceInUsed.objects.get(id=kwargs.get('pk'))
            old_volume, old_state = instance.volume, instance.state
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            Reports.objects.create(device=serializer.instance, 
                                   customer=customer,
                                   old_volume=old_volume,
                                   new_volume=serializer.data.get('volume'),
                                   old_state=old_state,
                                   new_state=serializer.data.get('state'))

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            return Response({"status": "User is not customer or User is not owner/member of the house"})

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
