from django.db import models
from accounts.models import Customer, Contractor
# from device_cntrl.models import Device
# Create your models here.


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
