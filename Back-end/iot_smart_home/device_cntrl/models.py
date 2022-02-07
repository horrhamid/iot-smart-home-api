from django.db import models
from home_cntrl.models import House
from accounts.models import Customer
from django_bleach.models import BleachField

# Create your models here.


class Device(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, null=True, blank=True)
    # cntrl_commands
    # default settings
    details = BleachField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    version = models.CharField(max_length=20, default='1.0.0')
    product_code = models.CharField(max_length=20, null=True, blank=True)
    firmware = models.FileField(upload_to='uploads/%Y-%m-%d/', null=True, blank=True)

    def __str__(self):
        return self.name


class DeviceInUsed(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    turn_on_time = models.TimeField(blank=True, null=True)
    turn_off_time = models.TimeField(blank=True, null=True)
    volume = models.CharField(max_length=8, default='NOT SET')
    state = models.CharField(max_length=8, default='NOT SET')

    def __str__(self):
        return self.device.name


class Reports(models.Model):
    device = models.ForeignKey(DeviceInUsed, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    old_volume = models.CharField(max_length=8, default='NOT SET')
    new_volume = models.CharField(max_length=8, default='NOT SET')
    old_state = models.CharField(max_length=8, default='NOT SET')
    new_state = models.CharField(max_length=8, default='NOT SET')
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return (self.device.device.name + ' ' + self.customer.user.username)


