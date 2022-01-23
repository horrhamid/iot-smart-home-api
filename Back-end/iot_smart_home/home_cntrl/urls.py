from django.urls import path, include
from rest_framework import routers

from .views import HouseView

router = routers.DefaultRouter()
router.register('house', HouseView, basename='Houses')
urlpatterns = [
    path('model/', include(router.urls)),
]