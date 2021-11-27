# Generated by Django 3.2.9 on 2021-11-27 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo_url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='醫師', max_length=100),
        ),
    ]
