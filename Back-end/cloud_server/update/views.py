from django.views.generic import ListView
from .models import FileUpdate
from django.http import JsonResponse
from django.views import View
from django.http import JsonResponse
import requests

class DownloadFile(ListView):
    model = FileUpdate

    def get(self, request, *args, **kwargs):
        latest_release_info = self.get_queryset().latest('created_date')
        data = {
            'version': latest_release_info.version,
            'file_path': latest_release_info.update_file.name,
            'release_date': latest_release_info.created_date
        }
        return JsonResponse(data)


class UpdateHomeView(View):

    def get(self, request, *args, **kwargs):
        try:
            instance = FileUpdate.objects.last()
            print('---instance: ', instance.version)
            response = requests.get("http://127.0.0.1:7000/update/send-update/")
            print('aft')
            return JsonResponse({'msg': 'Update exists', 'version': instance.version})
        except:
            return JsonResponse({'msg': 'Couldn\'t update home'}, status=404)