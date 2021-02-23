# Generated by Django 3.0.3 on 2021-02-23 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital', '0019_auto_20210222_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pledge',
            fields=[
                ('pledge_id', models.AutoField(primary_key=True, serialize=False)),
                ('pledge_name', models.CharField(max_length=50)),
                ('pledge_city', models.CharField(max_length=20)),
                ('pledge_mobile_no', models.CharField(max_length=10)),
                ('pledge_organ', models.CharField(default=None, max_length=50)),
                ('pledge_bloodGroup', models.CharField(max_length=10)),
                ('pledge_gender', models.CharField(max_length=10)),
                ('pledge_diseases', models.TextField(blank=True, max_length=100)),
                ('pledge_addiction', models.TextField(blank=True, max_length=100)),
                ('pledge_info', models.CharField(blank=True, max_length=200)),
                ('pledge_hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
            ],
        ),
    ]
