from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import phone_validator


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        UNSET = 'MF', 'Unset'
    ROLE_CHOISES = [
        ('Co', 'Contractor'),
        ('Cu', 'Customer')
    ]
    phone = models.CharField(max_length=15, validators=[phone_validator], blank=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSET)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    role = models.CharField(blank=True, null=True, max_length=2, choices=ROLE_CHOISES)
    avatar = models.ImageField(verbose_name='avatar', null=True, blank=True)


class Contractor(models.Model):
    salary = models.FloatField(null=False, default=0.00)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contractor')
    under_service_area = models.TextField(blank=True, null=True)
    resume = models.TextField(blank=True, null=True)
    # messages


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    # preferences
    # personalization
