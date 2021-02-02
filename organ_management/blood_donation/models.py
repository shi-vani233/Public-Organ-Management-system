from django.db import models

class Volunteer(models.Model):
    volunteer_email=models.CharField(max_length=50,primary_key=True,help_text ='write your email')
    volunteer_name=models.CharField(max_length=30)
    volunteer_city=models.CharField(max_length=20)
    volunteer_mobile_no=models.CharField(max_length=10)
    volunteer_bloodGroup=models.CharField(max_length=10,default=None)
    volunteer_gender=models.CharField(max_length=10,default=None)
    


