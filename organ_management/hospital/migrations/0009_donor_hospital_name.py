# Generated by Django 3.1.5 on 2021-02-04 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_remove_donor_hospital_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='hospital_name',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
