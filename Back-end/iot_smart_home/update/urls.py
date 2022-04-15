from django.urls import path
from .views import *


urlpatterns = [
    path('receive-update-notification', ReceiveUpdateNotification.as_view()),
    path('send-update/', UpdateAllFiles.as_view()),
    path('restore-update/', RestoreAllFiles.as_view()),
    path('device-update/', UpdateDeviceFiles.as_view()),
]
