from django.db.models.fields import DateTimeField, EmailField
from django.http.response import JsonResponse
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
from hospital.models import Hospital,Donor, OrganRequest
import simplejson as json
import datetime

global ChangedState

def Mainpage(request):
    hospitals=Hospital.objects.all()
    return render(request, 'main.html', {'hospitals':hospitals})

def registerpage(request):
    return render(request, 'register.html', context=None)

def loginpage(request):
    c = {} 
    c.update(csrf(request))
    return render(request, 'login.html', context=None)

def hospitalHome(request):
    if request.user.is_authenticated:
        return render(request, 'hospitalHome.html', context=None)
    else:
        return HttpResponseRedirect('/Hospital/Mainpage/')


def registerhospital(request):
    hospital_email=request.POST.get('hospital_email','')
    hospital_name=request.POST.get('hospital_name','')
    hospital_city=request.POST.get('hospital_city','')
    hospital_mobile_no=request.POST.get('hospital_mobile_no','')
    hospital_address=request.POST.get('hospital_address','')
    zip_code=request.POST.get('zip_code','')
    password=request.POST.get('password','')
    repassword=request.POST.get('repassword','')
    if password!=repassword or len(password)<6:
        msg_pass="password and confirm password must be same with minimum length 6"
    else:
        msg_pass=''
    if len(hospital_mobile_no)!=10:
        msg_phone="phone number must be of length 10"
    else:
        msg_phone=''
    if len(zip_code) != 6:
        msg_zip="pin code must be of length 6"
    else:
        msg_zip=''
    hospitals=Hospital.objects.all()
    if not (msg_pass or msg_phone or msg_zip):
        try:
            user=User.objects.create_user(username=hospital_email,email=hospital_email,password=password)
            #user.set_password(password)
            user.save()
            hosp=Hospital(hospital_email=hospital_email,hospital_name=hospital_name,hospital_city=hospital_city,
                hospital_mobile_no=hospital_mobile_no,hospital_address=hospital_address,zip_code=zip_code)
            hosp.save()
            msg="you are successfully registered, Go for Login!"
            return render(request ,'main.html',{'msg':msg,'hospitals':hospitals})
        except:
            msg_error="this email is already registered"
            return render(request,'register.html',{'msg_error':msg_error})
    else:
        return render(request ,'register.html',{'msg_pass':msg_pass,'msg_phone':msg_phone,'msg_zip':msg_zip})


def loginhospital(request):
    hospital_email=request.POST.get('hospital_email','')
    password=request.POST.get('password','')
    User=auth.authenticate(username=hospital_email,password=password)
    if User is not None:
        auth.login(request,User)
        return HttpResponseRedirect('/Hospital/Home')
    else:
        msg = "Invalid Username or Password!"
        return render(request,'login.html',{'msg_login':msg})
        

def logout(request):

    auth.logout(request)
    return redirect('/Hospital/Mainpage/')

def add_donor(request):
    
    if request.user.is_authenticated:
        donor_name=request.POST.get('donor_name','')
        donor_dob=request.POST.get('donor_dob','')
        donor_organ=request.POST.get('donor_organ','')
        donor_height=request.POST.get('donor_height','')
        donor_weight=request.POST.get('donor_weight','')
        donor_bloodGroup=request.POST.get('donor_bloodGroup','')
        donor_gender=request.POST.get('donor_gender','')
        donor_info=request.POST.get('donor_info','')
        donor_diseases=request.POST.getlist('donor_diseases','')
        donor_addiction=request.POST.getlist('donor_addiction','')
        donor_added_time=datetime.datetime.now() 
        hospital_email=request.user.username
        print(type(donor_diseases))
        don=Donor(donor_name=donor_name,
                    donor_dob=donor_dob,
                    donor_organ=donor_organ,
                    donor_height=donor_height,
                    donor_weight=donor_weight,
                    donor_bloodGroup=donor_bloodGroup,
                    donor_gender=donor_gender,
                    donor_info=donor_info,
                    donor_diseases = donor_diseases,
                    donor_addiction = donor_addiction,
                    donor_added_time=donor_added_time,
                    hospital_email=hospital_email,
                    )
        don.save()
    
    msg_donor="Donor added successfully!"
    return render(request, 'hospitalHome.html',{'msg_donor':msg_donor})

def DonorList(request):
    if request.user.is_authenticated:
        hospital_email=request.user.username

        don=Donor.objects.filter(hospital_email=hospital_email)
        # for i in don:
        #     print(i.donor_diseases)
        # print("..............................")
        return render(request, 'donorList.html', {'don':don})

def PotentialDonorList(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        don=Donor.objects.exclude(hospital_email=loggedin_user)
        hos=Hospital.objects.exclude(hospital_email=loggedin_user)
        return render(request,'potentialDonor.html',{'other_donors':don,'hos':hos})


def DonorDetails(request):
    if request.user.is_authenticated:
    #got donor_id from template by hidden field
        loggedin_user=request.user.username
        getid=request.POST.get('id','')
        donor=Donor.objects.get(donor_id=getid)
        hos=Hospital.objects.exclude(hospital_email=loggedin_user)
        temp = donor.hospital_email
        reciever = Hospital.objects.get(hospital_email=temp)
        loggedin_user=request.user.username
        sender = Hospital.objects.get(hospital_email=loggedin_user)
        obj = OrganRequest.objects.filter(sender=sender, reciever=reciever)
        if obj.exists():
            ChangedState = True
        else:
            ChangedState = False
        return render(request, 'donordetails.html',{'donor':donor,'hos':hos, 'ChangedState':ChangedState})

def SendRequest(request):
    if request.user.is_authenticated:
        getid=request.POST.get('id','')
        donor=Donor.objects.get(donor_id=getid)
        temp = donor.hospital_email
        reciever = Hospital.objects.get(hospital_email=temp)
        loggedin_user=request.user.username
        sender = Hospital.objects.get(hospital_email=loggedin_user)
        req = OrganRequest(sender=sender, reciever=reciever)
        req.save()
        msg="Request Successfully Sent"
        ChangedState = True
        hos=Hospital.objects.exclude(hospital_email=loggedin_user)
        return render(request, 'donordetails.html',{'msg':msg, 'hos':hos, 'donor':donor, 'ChangedState':ChangedState})

def CancelRequest(request):
    if request.user.is_authenticated:
        getid=request.POST.get('id','')
        donor=Donor.objects.get(donor_id=getid)
        temp = donor.hospital_email
        reciever = Hospital.objects.get(hospital_email=temp)
        loggedin_user=request.user.username
        sender = Hospital.objects.get(hospital_email=loggedin_user)
        obj = OrganRequest.objects.filter(sender=sender, reciever=reciever)
        obj.delete()
        msg="Request Successfully Deleted"
        ChangedState = False
        hos=Hospital.objects.exclude(hospital_email=loggedin_user)
        return render(request, 'donordetails.html',{'msg':msg, 'hos':hos, 'donor':donor, 'ChangedState':ChangedState})