# Generated by Django 3.1.5 on 2021-02-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation', '0005_auto_20210202_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='volunteer_bloodGroup',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
