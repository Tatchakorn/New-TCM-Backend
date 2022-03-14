from django.db import models

# Create your models here.

class PulseOption(models.Model):
    
    option = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'PulseOption'
        verbose_name_plural = 'PulseOptions'

    def __str__(self):
        return self.name


class WenOptionCategory(models.Model):

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'WenOptionCategory'
        verbose_name_plural = 'WenOptionCategories'

    def __str__(self):
        return self.name


class WenOption(models.Model):

    option = models.CharField(max_length=64)
    category = models.ForeignKey(
        WenOptionCategory,
        related_name='wen_category',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'WenOptionCategory'
        verbose_name_plural = 'WenOptionCategories'

    def __str__(self):
        return self.name


class WangOptionCategory(models.Model):

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'WangOptionCategory'
        verbose_name_plural = 'WangOptionCategories'

    def __str__(self):
        return self.name


class WangOption(models.Model):

    option = models.CharField(max_length=64)
    category = models.ForeignKey(
        WangOptionCategory,
        related_name='wang_category',
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'WangOption'
        verbose_name_plural = 'WangOptions'

    def __str__(self):
        return self.name


class DiseaseOptionCategory(models.Model):

    name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'DiseaseCategory'
        verbose_name_plural = 'DiseaseCategories'

    def __str__(self):
        return self.name


class DiseaseOption(models.Model):

    option = models.CharField(max_length=64)
    category = models.ForeignKey(
        DiseaseOptionCategory,
        related_name='disease_category',
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'DiseaseOption'
        verbose_name_plural = 'DiseaseOptions'

    def __str__(self):
        return self.name