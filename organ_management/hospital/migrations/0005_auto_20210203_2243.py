# Generated by Django 3.0.3 on 2021-02-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_donor_donor_organ'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='hospital_email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_addiction',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='donor',
            name='donor_diseases',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
