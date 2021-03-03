from django.urls import path
from blood_donation.views import BloodDonationHome,VolunteerPage,Registervol,searchBloodGroup,VolunteerList
from django.conf.urls import url,include

urlpatterns = [
    url('BloodDonationHome/',BloodDonationHome),
    url('Volunteer/',VolunteerPage),
    url(r'^Registervol/',Registervol),
    url(r'^VolunteerList/',VolunteerList),
    url(r'^searchBloodGroup/',searchBloodGroup),
]