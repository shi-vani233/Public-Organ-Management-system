# Generated by Django 3.0.3 on 2021-02-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_auto_20210203_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='donor_organ',
            field=models.CharField(default=None, max_length=50),
        ),
    ]