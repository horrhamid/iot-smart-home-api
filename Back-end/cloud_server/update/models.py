from django.db import models


class FileUpdate(models.Model):
    version = models.CharField(max_length=15)
    update_file = models.FileField(upload_to='uploads/%Y-%m-%d/')
    created_date = models.DateTimeField(auto_now_add=True)
