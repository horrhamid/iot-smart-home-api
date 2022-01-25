from django.views.generic import ListView
from .models import FileUpdate
from django.http import JsonResponse


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
