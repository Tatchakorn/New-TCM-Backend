# Generated by Django 3.2.9 on 2022-06-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_othermedia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosisrecord',
            name='disease_name',
        ),
        migrations.AddField(
            model_name='diagnosisrecord',
            name='codisease_icd_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='diagnosisrecord',
            name='codisease_icd_code_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='diagnosisrecord',
            name='decoction_cook_way',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='diagnosisrecord',
            name='decoction_pack_amout',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='diagnosisrecord',
            name='decoction_total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='diagnosisrecord',
            name='decoction_way',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='diagnosisrecord',
            name='disease_icd_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='diagnosisrecord',
            name='medicine_way',
            field=models.TextField(blank=True, null=True),
        ),
    ]
