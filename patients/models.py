from django.db import models
from django.db.models.base import Model
from django.utils import timezone
from rest_framework import serializers


class PatientsInfo(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M', ('男')
        FEMALE = 'F', ('女')

    name = models.CharField(max_length=250)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE
    )
    arrears = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    card_id = models.CharField(max_length=200)
    consultation_no = models.IntegerField()
    department = models.CharField(max_length=200)
    medical_order_number = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    period = models.IntegerField()
    register_time = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True)
    selected = models.BooleanField(default=False)
    status = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class DiagnosisInfo(models.Model):
    patient = models.ForeignKey(
        PatientsInfo,
        related_name='diagnosis',
        on_delete=models.CASCADE)
    diagnosis_data = models.JSONField(default=dict)


class YanImages(models.Model):
    diagnosis = models.ForeignKey(
        DiagnosisInfo,
        related_name='yan_imgs',
        on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/yan', null=True)
    date = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True)


class SheImages(models.Model):
    diagnosis = models.ForeignKey(
        DiagnosisInfo,
        related_name='she_imgs',
        on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/she', null=True)
    date = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length=200, blank=True, null=True)
