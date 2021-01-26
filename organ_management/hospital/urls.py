from django.urls import path
from hospital.views import Mainpage,Login,hospitalHome,DonorList,PotentialDonorList,profile_view,CustomUserUpdateView,CustomUserDeleteView
from django.conf.urls import url

urlpatterns = [
    url('Mainpage/',Mainpage),
    url('Home/',hospitalHome),
    url('donorList/',DonorList),
    url('potentialDonor/',PotentialDonorList),
    url('Login/',Login),
    url('profile/', profile_view, name='account_profile'),
    path('<int:pk>/update/', CustomUserUpdateView.as_view(template_name='account/update.html'), name='account_update'),
    path('<int:pk>/delete/', CustomUserDeleteView.as_view(template_name='account/delete.html'), name='account_delete'),
    
]