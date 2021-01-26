from django.urls import path
from hospital.views import Mainpage,Login,hospitalHome,DonorList,PotentialDonorList,profile_view
from django.conf.urls import url

urlpatterns = [
    url('Mainpage/',Mainpage),
    url('Home/',hospitalHome),
    url('donorList/',DonorList),
    url('potentialDonor/',PotentialDonorList),
    url('Login/',Login),
    url('profile/', profile_view, name='account_profile')
    
]