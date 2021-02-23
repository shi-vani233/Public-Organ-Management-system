from django.urls import path
from home.views import Homepage, DonorPledge
from django.conf.urls import url

urlpatterns = [
    url('Homepage/',Homepage),
    url(r'^DonorPledge/',DonorPledge)
]