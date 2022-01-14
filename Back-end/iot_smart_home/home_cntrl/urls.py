from django.urls import path, include
from rest_framework import routers

from .views import HouseView

# snippet_detail = HomeManagement.as_view({
#     'get': 'list',
# })

router = routers.DefaultRouter()
router.register('house', HouseView, basename='Houses')
# router.register('pppp', HomeManagement, basename='House')
# router.register(r'manage', HomeManagement, basename='dev')
# router.register('manage/', HomeManagement, basename='Home')
urlpatterns = [
    path('model/', include(router.urls)),
    # path('manage/', snippet_detail, name='snippet_detail'),
    # path('manage/', HomeManagement),
]