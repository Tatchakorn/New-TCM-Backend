from django.utils import timezone
from django.db import models


class Pulse(models.Model):
    data = models.JSONField()
    remarks = models.CharField(max_length=256)
    time = models.DateTimeField(default=timezone.now)