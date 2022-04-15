from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests


class FileUpdate(models.Model):
    version = models.CharField(max_length=15)
    update_file = models.FileField(upload_to='uploads/%Y-%m-%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.version


@receiver(post_save, sender=FileUpdate)
def send_notification(sender, instance, created, **kwargs):
    if created:
        response = requests.get("http://127.0.0.1:7000/update/receive-update-notification", params={'version': instance.version})
        print(response.json())