from django.urls import path, include
from rest_framework import routers

from .views import Dashboard, HomeManagement

# snippet_detail = HomeManagement.as_view({
#     'get': 'list',
# })

router = routers.DefaultRouter()
router.register('', Dashboard, basename='Houses')
# router.register(r'manage', HomeManagement, basename='dev')
# router.register('manage/', HomeManagement, basename='Home')
urlpatterns = [
    path('', include(router.urls)),
    # path('manage/', snippet_detail, name='snippet_detail'),
    path('manage/', HomeManagement),
]