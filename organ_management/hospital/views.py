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
from hospital.models import Hospital

def Mainpage(request):

    hospitals=Hospital.objects.all()
    return render(request, 'main.html', {'hospitals':hospitals})

def DonorList(request):
    return render(request, 'donorList.html', context=None)

def PotentialDonorList(request):
    return render(request, 'potentialDonor.html', context=None)

def Login(request):
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
    if not (msg_pass or msg_phone or msg_zip):
        try:
            user=User.objects.create_user(username=hospital_email,email=hospital_email)
            user.set_password(password)
            user.save()
            hosp=Hospital(hospital_email=hospital_email,hospital_name=hospital_name,hospital_city=hospital_city,
                hospital_mobile_no=hospital_mobile_no,hospital_address=hospital_address,zip_code=zip_code)
            hosp.save()
            msg="you are successfully registered, Go for Login!"
            return render(request ,'main.html',{'msg':msg})
        except:
            msg_error="this email already registered"
            return render(request,'main.html',{'msg_error':msg_error})
    else:
        return render(request ,'main.html',{'msg_pass':msg_pass,'msg_phone':msg_phone,'msg_zip':msg_zip})

def loginhospital(request):

    hospital_email=request.POST.get('hospital_email','')
    password=request.POST.get('password','')
    User=auth.authenticate(username=hospital_email,password=password)
    
    if User is not None:
        auth.login(request,User)
        return HttpResponseRedirect('/Hospital/Home')
    else:
        msg = "Invalid Username or Password!"
        print("wrongpass==========")
        return render(request,'main.html',{'msg_login':msg})

def logout(request):

    auth.logout(request)
    return redirect('/Hospital/Mainpage/')


