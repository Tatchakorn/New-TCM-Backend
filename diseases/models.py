from django.db import models


class Diseases(models.Model):
    code = models.CharField(max_length=32)
    ch_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
