from django.db import models

class Medicines(models.Model):
    bapomofo = models.CharField(max_length=8)
    name = models.CharField(max_length=256)
    info = models.JSONField(default=dict)


# class FangMedicines(models.Model):
#     ...


# class YaoMedicines(models.Model):
#     ...

    