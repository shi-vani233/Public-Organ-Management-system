from django.urls import path
from hospital.views import Mainpage,Login,hospitalHome,DonorList,PotentialDonorList,registerhospital,loginhospital,logout
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('Mainpage/',Mainpage),
    url('Home/',hospitalHome),
    url('donorList/',DonorList),
    url('potentialDonor/',PotentialDonorList),
    url('Login/',Login),
    url(r'^registerhospital/',registerhospital),
    url(r'^loginhospital/',loginhospital),
    url(r'^logout/',logout),
]