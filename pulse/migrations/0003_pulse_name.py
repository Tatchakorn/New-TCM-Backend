# Generated by Django 3.2.9 on 2021-12-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pulse', '0002_alter_pulse_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='pulse',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
    ]