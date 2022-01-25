from django.urls import path
from .views import DownloadFile

urlpatterns = [
    path('download-file/', DownloadFile.as_view()),
]
