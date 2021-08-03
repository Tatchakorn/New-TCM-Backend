from django.db import models


class PatientsInfo(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', ('Male')
        FEMALE = 'F', ('Female')

    name = models.CharField(max_length=250)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.MALE
    )
    medical_record_number = models.IntegerField()
    date_of_birth = models.DateField()
    insurance_type = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
