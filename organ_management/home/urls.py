from django.urls import path
from home.views import Homepage,Volunteer
from django.conf.urls import url

urlpatterns = [
    url('Homepage/',Homepage),
    url('Volunteer/',Volunteer),
]