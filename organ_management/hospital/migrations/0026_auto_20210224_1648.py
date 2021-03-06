# Generated by Django 3.0.3 on 2021-02-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0025_donation'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Donation',
        ),
        migrations.AlterField(
            model_name='transplant',
            name='eye',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transplant',
            name='heart',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transplant',
            name='intestine',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transplant',
            name='kidney',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transplant',
            name='liver',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transplant',
            name='lung',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transplant',
            name='pancreas',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transplant',
            name='skin',
            field=models.IntegerField(default=0),
        ),
    ]
