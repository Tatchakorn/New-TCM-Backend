# Generated by Django 3.2.7 on 2021-10-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases', fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('code', models.CharField(
                        max_length=32)), ('ch_name', models.CharField(
                            max_length=255)), ('en_name', models.CharField(
                                max_length=255)), ], ), ]