from django.db import models
from hospital.models import Hospital

# Create your models here.
class Pledge(models.Model):
    pledge_id=models.AutoField(primary_key=True)
    pledge_name=models.CharField(max_length=50)
    pledge_city=models.CharField(max_length=20)
    pledge_mobile_no=models.CharField(max_length=10)
    pledge_organ=models.CharField(max_length=50,default=None)
    pledge_bloodGroup=models.CharField(max_length=10)
    pledge_gender=models.CharField(max_length=10)
    pledge_diseases=models.TextField(max_length=100,blank=True)
    pledge_addiction=models.TextField(max_length=100,blank=True)
    pledge_info=models.CharField(max_length=200,blank=True)
    pledge_hospital = models.ForeignKey(Hospital,on_delete=models.CASCADE)