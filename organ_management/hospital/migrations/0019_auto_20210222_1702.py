# Generated by Django 3.1.5 on 2021-02-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20210222_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='hospital_latitude',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='hospital',
            name='hospital_longitude',
            field=models.FloatField(default=None),
        ),
    ]
