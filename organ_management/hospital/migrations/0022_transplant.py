# Generated by Django 3.0.3 on 2021-02-23 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_delete_trends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transplant',
            fields=[
                ('trend_id', models.AutoField(primary_key=True, serialize=False)),
                ('kidney', models.CharField(max_length=30)),
                ('liver', models.CharField(max_length=30)),
                ('eye', models.CharField(max_length=30)),
                ('skin', models.CharField(max_length=30)),
                ('heart', models.CharField(max_length=30)),
                ('pancreas', models.CharField(max_length=30)),
                ('lung', models.CharField(max_length=30)),
                ('intestine', models.CharField(max_length=30)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
            ],
        ),
    ]