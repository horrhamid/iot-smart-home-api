from django.urls import path, include
from rest_framework import routers

from .views import Dashboard

router = routers.DefaultRouter()
router.register('', Dashboard, basename='Houses')
urlpatterns = [
    path('', include(router.urls)),
    path('manage/', include('device_cntrl.urls')),

]