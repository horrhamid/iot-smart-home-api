from django.urls import path
from .views import DownloadFile, UpdateHomeView

urlpatterns = [
    path('download-file/', DownloadFile.as_view()),
    path('fog-error/', UpdateHomeView.as_view())
]
