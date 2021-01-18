from django.urls import path
from home.views import Homepage
from django.conf.urls import url

urlpatterns = [
    url('Home/',Homepage),
]