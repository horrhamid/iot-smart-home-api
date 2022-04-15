from django.views import View
from .models import SaveUpdateNotification
from django.http import JsonResponse
import subprocess


class ReceiveUpdateNotification(View):

    def get(self, request, *args, **kwargs):
        version = request.GET.get('version')
        SaveUpdateNotification(is_applied=False, version=version).save()
        return JsonResponse({'Message': 'Device report is fetched'})


class UpdateAllFiles(View):

    def get(self, request, *args, **kwargs):
        subprocess.run(['fab', 'deploy_migrations'])
        return JsonResponse({'Message': 'Files updated'})


class RestoreAllFiles(View):

    def get(self, request, *args, **kwargs):
        subprocess.run(['fab', 'restore_update'])
        return JsonResponse({'Message': 'Files restored'})


class UpdateDeviceFiles(View):

    def get(self, request, *args, **kwargs):
        subprocess.run(['fab', 'partially_update'])
        return JsonResponse({'Message': 'Device Files updated'})
