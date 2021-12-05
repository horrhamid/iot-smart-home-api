
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserRegistration, LogoutAPIView, CustomerRegistration, ContractorRegistration

urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutAPIView.as_view()),
    path('register/', UserRegistration.as_view()),
    path('customer/', CustomerRegistration.as_view()),
    path('contractor/', ContractorRegistration.as_view()),
]