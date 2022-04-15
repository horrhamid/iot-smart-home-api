from django.db import models


class Update(models.Model):
    is_applied = models.BooleanField(default=False)
    received_at = models.DateTimeField(auto_now_add=True)
    version = models.CharField(max_length=15, blank=True, null=True)

