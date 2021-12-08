from django.db import models


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



