from django.db import models

class Hospital(models.Model):
    hospital_email=models.CharField(max_length=50,primary_key=True,help_text ='write your email')
    hospital_name=models.CharField(max_length=30)
    hospital_city=models.CharField(max_length=20)
    hospital_mobile_no=models.CharField(max_length=10)
    hospital_address=models.CharField(max_length=100,help_text = 'write your email')
    zip_code=models.CharField(max_length=6)

    


