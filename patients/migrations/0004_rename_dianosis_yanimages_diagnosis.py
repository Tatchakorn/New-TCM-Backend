# Generated by Django 3.2.7 on 2021-10-03 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20211003_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yanimages',
            old_name='dianosis',
            new_name='diagnosis',
        ),
    ]
