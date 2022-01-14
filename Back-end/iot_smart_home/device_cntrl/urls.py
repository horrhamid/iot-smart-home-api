from django.urls import path, include
from rest_framework import routers
from .views import DeviceView, DeviceInUsedView

router = routers.DefaultRouter()
router.register('device', DeviceView, basename='devices')
router.register('deviceinused', DeviceInUsedView, basename='deviceinused')
# router.register('pppp', HomeManagement, basename='House')


urlpatterns = [
    path('model/', include(router.urls)),
]