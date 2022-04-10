from django.db import models


class OptionModel(models.Model):
    option = models.CharField(max_length=64)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.option


class CategoryModel(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.name


class PulseOption(OptionModel):

    class Meta:
        verbose_name = 'PulseOption'
        verbose_name_plural = 'PulseOptions'


class WenOptionCategory(CategoryModel):

    class Meta:
        verbose_name = 'WenOptionCategory'
        verbose_name_plural = 'WenOptionCategories'


class WenOption(OptionModel):

    category = models.ForeignKey(
        WenOptionCategory,
        related_name='wen_category',
        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'WenOptionCategory'
        verbose_name_plural = 'WenOptionCategories'


class WangOptionCategory(CategoryModel):

    class Meta:
        verbose_name = 'WangOptionCategory'
        verbose_name_plural = 'WangOptionCategories'


class WangOption(OptionModel):

    category = models.ForeignKey(
        WangOptionCategory,
        related_name='wang_category',
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'WangOption'
        verbose_name_plural = 'WangOptions'



class DiseaseOptionCategory(CategoryModel):

    class Meta:
        verbose_name = 'DiseaseCategory'
        verbose_name_plural = 'DiseaseCategories'


class DiseaseOption(OptionModel):

    category = models.ForeignKey(
        DiseaseOptionCategory,
        related_name='disease_category',
        on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'DiseaseOption'
        verbose_name_plural = 'DiseaseOptions'


class EyeCategory(CategoryModel):

    class Meta:
        db_table = 'EyeCategory'
        verbose_name = 'EyeCategory'
        verbose_name_plural = 'EyeCategories'


class EyeOption(OptionModel):
    category = models.ForeignKey(
        EyeCategory,
        related_name='eye_category',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'EyeOption'
        verbose_name = 'EyeOption'
        verbose_name_plural = 'EyeOptions'


class TongueCategory(CategoryModel):

    class Meta:
        db_table = 'TongueCategory'
        verbose_name = 'TongueCategory'
        verbose_name_plural = 'TongueCategories'


class TongueOption(OptionModel):
    category = models.ForeignKey(
        TongueCategory,
        related_name='tongue_category',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'TongueOption'
        verbose_name = 'TongueOption'
        verbose_name_plural = 'TongueOptions'