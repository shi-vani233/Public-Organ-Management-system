# Generated by Django 3.1.5 on 2021-02-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0015_organrequest_pending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organrequest',
            name='organ_request_time',
            field=models.DateTimeField(default=None),
        ),
    ]