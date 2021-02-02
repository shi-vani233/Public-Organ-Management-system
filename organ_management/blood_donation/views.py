from django.db.models.fields import EmailField
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.core.mail import send_mail
from blood_donation.models import Volunteer

# Create your views here.
def BloodDonationHome(request):
    return render(request, 'BloodDonation.html', context=None)

def VolunteerPage(request):
    return render(request, 'volunteer.html', context=None)

def Registervol(request):
    volunteer_email=request.POST.get('volunteer_email','')
    volunteer_name=request.POST.get('volunteer_name','')
    volunteer_city=request.POST.get('volunteer_city','')
    volunteer_mobile_no=request.POST.get('volunteer_mobile_no','')
    volunteer_bloodGroup=request.POST.get('volunteer_bloodGroup','')
    volunteer_gender=request.POST.get('volunteer_gender','')
    print(volunteer_email)
    vol=Volunteer(volunteer_name=volunteer_name,volunteer_email=volunteer_email,volunteer_city=volunteer_city,
    volunteer_mobile_no=volunteer_mobile_no,volunteer_bloodGroup=volunteer_bloodGroup,volunteer_gender=volunteer_gender)
    vol.save()
    msg="You are registered!"
    return render(request,'volunteer.html',{'msg':msg})
