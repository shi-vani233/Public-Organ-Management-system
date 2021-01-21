from django.urls import path
from blood_donation.views import BloodDonationHome,Volunteer
from django.conf.urls import url

urlpatterns = [
    url('BloodDonationHome/',BloodDonationHome),
    url('Volunteer/',Volunteer)
]