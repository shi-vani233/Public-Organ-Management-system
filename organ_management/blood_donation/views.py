from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
from django.db.models import Q

# Create your views here.
def BloodDonationHome(request):
    return render(request, 'BloodDonation.html', context=None)

def VolunteerPage(request):
    volunteers=Volunteer.objects.all()
    return render(request, 'volunteer.html',  {'volunteers':volunteers})

def Registervol(request):
    volunteer_email=request.POST.get('volunteer_email','')
    volunteer_name=request.POST.get('volunteer_name','')
    volunteer_city=request.POST.get('volunteer_city','')
    volunteer_mobile_no=request.POST.get('volunteer_mobile_no','')
    volunteer_bloodGroup=request.POST.get('volunteer_bloodGroup','')
    volunteer_gender=request.POST.get('volunteer_gender','')
    print(volunteer_email)
    volunteers=Volunteer.objects.all()
    donor = Volunteer.objects.filter(volunteer_email=volunteer_email)
    if len(volunteer_mobile_no)!=10:
        msg_phone="phone number must be of length 10, please fill the form again with correct contact no"
    else:
        msg_phone=''
    if donor.exists() :
        msg_email = "This email is already registered"
    else:
        msg_email = ''
    if not ( msg_phone or msg_email ):
        vol=Volunteer(volunteer_name=volunteer_name,volunteer_email=volunteer_email,volunteer_city=volunteer_city,
        volunteer_mobile_no=volunteer_mobile_no,volunteer_bloodGroup=volunteer_bloodGroup,volunteer_gender=volunteer_gender)
        vol.save()
        msg="You are registered!"
        return render(request,'volunteer.html',{'msg':msg, 'volunteers':volunteers})
    else:
        return render(request ,'volunteer.html',{'msg_phone':msg_phone, 'msg_email':msg_email, 'volunteers':volunteers})

def VolunteerList(request):
    volunteers=Volunteer.objects.all()

    if volunteers.exists():
        paginator = Paginator(volunteers,5)
        page = request.GET.get('page', 1)
        try:
            volunteerss = paginator.page(page)
        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        return render(request, 'VolunteerList.html', {'volunteers':volunteerss})
    return render(request, 'VolunteerList.html')

def searchBloodGroup(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')
        if query=="" or request.GET.get('page')!=None:
            return VolunteerList(request)
       
        if query is not None:
            lookups= Q(volunteer_bloodGroup__icontains=query) | Q(volunteer_city__icontains=query) | Q(volunteer_name__icontains=query)

            results= Volunteer.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'VolunteerList.html', context)
