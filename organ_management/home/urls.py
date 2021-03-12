from django.urls import path
from home.views import Homepage, DonorPledge
from django.conf.urls import url,include
from blood_donation import views as bd_views
from . import views

urlpatterns = [
    # url('',Homepage),
    url(r'^DonorPledge/',DonorPledge),
    # path('Blood_Donation/BloodDonationHome/',bd_views.BloodDonationHome,name='BloodDonationHome'),
    path('',views.Homepage,name='home'),
]