# Generated by Django 3.1.5 on 2021-02-22 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0017_auto_20210222_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='hospital_latitude',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='hospital_longitude',
        ),
    ]