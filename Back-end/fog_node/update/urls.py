from django.urls import path
from .views import HomeUpdateStatusView


urlpatterns = [
    path('status/home', HomeUpdateStatusView.as_view()),
]