
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from two_factor.urls import urlpatterns as tf_urls
from .views import UserRegistration, LogoutAPIView, CustomerRegistration, ContractorRegistration

urlpatterns = [
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('customer/', CustomerRegistration.as_view()),
    path('contractor/', ContractorRegistration.as_view()),
    path('', include(tf_urls)),
]
