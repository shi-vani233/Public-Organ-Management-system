from django.urls import path
from home.views import Homepage,BloodDonation,Volunteer
from django.conf.urls import url

urlpatterns = [
    url('Homepage/',Homepage),
    url('BloodDonation/',BloodDonation),
     url('Volunteer/',Volunteer)
]