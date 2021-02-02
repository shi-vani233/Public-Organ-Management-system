from django.urls import path
from blood_donation.views import BloodDonationHome,VolunteerPage,Registervol
from django.conf.urls import url

urlpatterns = [
    url('BloodDonationHome/',BloodDonationHome),
    url('Volunteer/',VolunteerPage),
    url(r'^Registervol/',Registervol)
]