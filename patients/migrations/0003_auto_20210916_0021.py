# Generated by Django 3.2.7 on 2021-09-16 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_alter_diagnosisinfo_gan_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosisinfo',
            name='gan_img',
            field=models.ImageField(null=True, upload_to='yan'),
        ),
        migrations.AlterField(
            model_name='diagnosisinfo',
            name='she_img',
            field=models.ImageField(null=True, upload_to='she'),
        ),
    ]
