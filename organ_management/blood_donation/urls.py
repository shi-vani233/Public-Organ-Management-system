from django.urls import path
from blood_donation.views import BloodDonationHome,VolunteerPage,Registervol,searchBloodGroup
from django.conf.urls import url,include

urlpatterns = [
    url('BloodDonationHome/',BloodDonationHome),
    url('Volunteer/',VolunteerPage),
    url(r'^Registervol/',Registervol),
    url(r'^searchBloodGroup/',searchBloodGroup),
]