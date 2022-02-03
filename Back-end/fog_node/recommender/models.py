from django.db import models
from django_bleach.models import BleachField
from accounts.models import Customer, Contractor



class House(models.Model):
    post_code = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='own_house')
    members = models.ManyToManyField(Customer, related_name='house_member')
    main_contractor = models.ForeignKey(Contractor, on_delete=models.SET_NULL, blank=True, null=True)
    # devices = models.ManyToManyField(Device, related_name='used_home')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.post_code or ''


class Device(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50, null=True, blank=True)
    # cntrl_commands
    # default settings
    details = BleachField(null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
    version = models.CharField(max_length=20, default='1.0.0')
    product_code = models.CharField(max_length=20, null=True, blank=True)

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


