from django.db import models

class Hospital(models.Model):
    hospital_email=models.CharField(max_length=50,primary_key=True,help_text ='write your email')
    hospital_name=models.CharField(max_length=30)
    hospital_city=models.CharField(max_length=20)
    hospital_mobile_no=models.CharField(max_length=10)
    hospital_address=models.CharField(max_length=100,help_text = 'write your email')
    zip_code=models.CharField(max_length=6)

class Donor(models.Model):
    donor_id=models.AutoField(primary_key=True)
    hospital_email=models.CharField(max_length=50,default=None)
    donor_name=models.CharField(max_length=50)
    donor_dob=models.DateTimeField()
    donor_organ=models.CharField(max_length=50,default=None)
    donor_height=models.CharField(max_length=50)
    donor_weight=models.CharField(max_length=50)
    donor_bloodGroup=models.CharField(max_length=10)
    donor_gender=models.CharField(max_length=10)
    donor_diseases=models.TextField(max_length=100,blank=True)
    donor_addiction=models.TextField(max_length=100,blank=True)
    donor_info=models.CharField(max_length=200,blank=True)
    donor_added_time=models.DateTimeField(default=None)
    models.ForeignKey(Hospital,on_delete=models.CASCADE)
    class Meta:
        unique_together = ('donor_id','hospital_email')

    


