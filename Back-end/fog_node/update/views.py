from django.views import View
from rest_framework import status
from django.http import JsonResponse
from .serializers import HomeUpdateStatusSerializer
from .models import Update
import requests


class HomeUpdateStatusView(View):

    def get(self, request, *args, **kwargs):
        try:
            instance = Update.objects.last()
            print('instance: ', instance.version)
            response = requests.get("http://127.0.0.1:7000/update/send-update/")
            return JsonResponse({'msg': 'Update exists', 'version': instance.version})
        except:
            print('sending error')
            response = requests.get("http://127.0.0.1:7000/update/restore-update/")
            response = requests.get("http://127.0.0.1:9000/update/fog-error/")
            return JsonResponse({'msg': 'Sending error to cloud'}, status=404)