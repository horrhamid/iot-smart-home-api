from django.db import models
from home_cntrl.models import House


# Create your models here.


class Device(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, null=True, blank=True)
    # cntrl_commands
    # default settings
    details = models.TextField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    version = models.CharField(max_length=20, default='1.0.0')
    product_code = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name


class DeviseInUsed(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    turn_on_time = models.TimeField(blank=True, null=True)
    turn_off_time = models.TimeField(blank=True, null=True)
    volume = models.CharField(max_length=8, default='NOT SET')
    state = models.CharField(max_length=8, default='NOT SET')


