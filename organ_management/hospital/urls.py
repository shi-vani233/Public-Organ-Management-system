from django.urls import path
from hospital.views import Mainpage, add_donor,hospitalHome,DonorList,PotentialDonorList,registerhospital,loginhospital,logout,registerpage,loginpage
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView

urlpatterns = [
    url('Mainpage/',Mainpage),
    url('Home/',hospitalHome),
    url('donorList/',DonorList),
    url('potentialDonor/',PotentialDonorList),
    url('registerpage/',registerpage),
    url('loginpage/',loginpage),
    url(r'^registerhospital/',registerhospital),
    url(r'^loginhospital/',loginhospital),
    url(r'^logout/',logout),
    url(r'^add_donor/',add_donor),

    path('password_reset/',PasswordResetView.as_view(template_name='password_reset.html'),name='password_reset'),
	path('password_reset/complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
	path('password_reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
	path('password_reset/done/',PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
]