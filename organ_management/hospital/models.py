from django.db import models

class Hospital(models.Model):
    hospital_email=models.CharField(max_length=50,primary_key=True,help_text ='write your email')
    hospital_name=models.CharField(max_length=30)
    hospital_city=models.CharField(max_length=20)
    hospital_mobile_no=models.CharField(max_length=10)
    hospital_address=models.CharField(max_length=100,help_text = 'write your email')
    zip_code=models.CharField(max_length=6)
    hospital_latitude=models.FloatField(default=None)
    hospital_longitude=models.FloatField(default=None)


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
    def __str__(self):
        return str(self.donor_added_time) 

class OrganRequest(models.Model):
    req_id=models.AutoField(primary_key=True)
    sender = models.ForeignKey(Hospital,on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(Hospital,on_delete=models.CASCADE, related_name="reciever")
    donor = models.ForeignKey(Donor,on_delete=models.CASCADE, related_name="Donor",default=None)
    accepted = models.BooleanField(blank=True, null=False, default=False)
    declined = models.BooleanField(blank=True, null=False, default=False)
    pending = models.BooleanField(blank=True, null=False, default=True)
    organ_request_time=models.DateTimeField(default=None)

class Transplant(models.Model):
    trend_id=models.AutoField(primary_key=True)
    kidney=models.IntegerField(default=0)
    liver=models.IntegerField(default=0)
    eye=models.IntegerField(default=0)
    skin=models.IntegerField(default=0)
    heart=models.IntegerField(default=0)
    pancreas=models.IntegerField(default=0)
    lung=models.IntegerField(default=0)
    intestine=models.IntegerField(default=0)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE)


class Donation(models.Model):
    donation_id=models.AutoField(primary_key=True)
    donor_name=models.CharField(max_length=50)
    patient_name=models.CharField(max_length=50)
    organ=models.CharField(max_length=30)
    details_added_time=models.DateTimeField(default=None)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE)
