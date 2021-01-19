from django.urls import path
from home.views import Homepage,Volunteer
from django.conf.urls import url

urlpatterns = [
    url('Home/',Homepage),
    url('Volunteer/',Volunteer)
]