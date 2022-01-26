from django.urls import path, include
from rest_framework import routers

from .views import RecommenderView

router = routers.DefaultRouter()
router.register('reports', RecommenderView, basename='recommender')
urlpatterns = [
    path('model/', include(router.urls)),
]