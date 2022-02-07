from django.views import View
from .models import SaveUpdateNotification
from django.http import JsonResponse


class ReceiveUpdateNotification(View):

    def get(self, request, *args, **kwargs):
        SaveUpdateNotification(is_applied=False).save()
        return JsonResponse({'Message': 'New Update Available version: V.1.0.3'})
