# Generated by Django 3.2.7 on 2021-10-03 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_rename_dianosis_sheimages_diagnosis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosisinfo',
            name='patient',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='diagnosis',
                to='patients.patientsinfo'),
        ),
        migrations.AlterField(
            model_name='sheimages',
            name='diagnosis',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='she_imgs',
                to='patients.diagnosisinfo'),
        ),
        migrations.AlterField(
            model_name='yanimages',
            name='dianosis',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='yan_imgs',
                to='patients.diagnosisinfo'),
        ),
    ]
