from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOISES = [
        ('Co', 'Contractor'),
        ('Cu', 'Customer')
    ]
    role = models.CharField(blank=True, null=True, max_length=2, choices=ROLE_CHOISES)


class Contractor(models.Model):
    phone = models.CharField(max_length=15, blank=True, null=True)
    salary = models.FloatField(null=False, default=0.00)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    under_service_area = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    # messages


class Customer(models.Model):
    phone = models.CharField(max_length=15, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # preferences
    # personalization
