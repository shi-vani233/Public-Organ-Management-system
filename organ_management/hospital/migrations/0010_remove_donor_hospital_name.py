# Generated by Django 3.1.5 on 2021-02-04 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_donor_hospital_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='hospital_name',
        ),
    ]
