from django.urls import path
from .views import ReceiveUpdateNotification


urlpatterns = [
    path('receive-update-notification', ReceiveUpdateNotification.as_view())
]
