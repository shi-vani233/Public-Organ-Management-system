from typing import final
from django.db.models.fields import DateTimeField, EmailField
from django.http.response import HttpResponseNotAllowed, JsonResponse
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
from hospital.models import Hospital,Donor, OrganRequest, Transplant, Donation
import simplejson as json
import datetime
from geopy.geocoders import Nominatim
from geopy.distance import distance as geopy_distance
from django.db.models import Q
from home.models import Pledge

geolocator = Nominatim(user_agent="hospital")
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
        loggedin_user=request.user.username
        current_user = Hospital.objects.get(hospital_email=loggedin_user) 
        allreq = OrganRequest.objects.filter(reciever=current_user,accepted=False,declined=False)
        i=0
        for c in allreq:
            i=i+1
        return render(request, 'hospitalHome.html',{'i':i})
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
    a=hospital_address+" "
    b=hospital_city
    c=a+b
    location1 = geolocator.geocode(c)
    print(location1.address)
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
                hospital_mobile_no=hospital_mobile_no,hospital_address=hospital_address,zip_code=zip_code,
                hospital_latitude=location1.latitude,hospital_longitude=location1.longitude)
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
        
        today_datetime = datetime.datetime.now()
        today_date=today_datetime.strftime("%d")
        today_month=today_datetime.month
        today_year=today_datetime.year

        today_hour = today_datetime.hour
        temp1=[]
        for item in don:
            if item.donor_added_time.strftime("%d") == today_date and item.donor_added_time.month == today_month and item.donor_added_time.year == today_year :
                temp1.append(item)
            elif int(item.donor_added_time.strftime("%d"))+1 == int(today_date):
                print(item.donor_added_time.hour - today_hour)
                if item.donor_added_time.hour - today_hour < 24 and item.donor_added_time.hour - today_hour >= 0:
                    temp1.append(item)
        don=temp1
        allreadyaccepted=OrganRequest.objects.filter(accepted=True)
        if allreadyaccepted.exists():
            temp=[]
            for i in allreadyaccepted:
                for j in don:
                    if i.donor.donor_id != j.donor_id:
                        obj=Donor.objects.get(donor_id=j.donor_id)
                        temp.append(obj)
 
            return render(request,'potentialDonor.html',{'other_donors':temp,'hos':hos})     
               
        return render(request,'potentialDonor.html',{'other_donors':don,'hos':hos})


def SearchDonor(request):
    if request.user.is_authenticated:
        
        loggedin_user=request.user.username
        hos=Hospital.objects.exclude(hospital_email=loggedin_user)
        don=Donor.objects.exclude(hospital_email=loggedin_user)
        
        today_datetime = datetime.datetime.now()
        today_date=today_datetime.strftime("%d")
        today_month=today_datetime.month
        today_year=today_datetime.year

        today_hour = today_datetime.hour
        temp1=[]
        for item in don:
            if item.donor_added_time.strftime("%d") == today_date and item.donor_added_time.month == today_month and item.donor_added_time.year == today_year :
                temp1.append(item)
            elif int(item.donor_added_time.strftime("%d"))+1 == int(today_date):
                print(item.donor_added_time.hour - today_hour)
                if item.donor_added_time.hour - today_hour < 24 and item.donor_added_time.hour - today_hour >= 0:
                    temp1.append(item)
        don=temp1
        allreadyaccepted=OrganRequest.objects.filter(accepted=True)

        if request.method == 'GET':
            query= request.GET.get('q')
            submitbutton= request.GET.get('submit')

            if query=="":
                if allreadyaccepted.exists():
                    temp=[]
                    for i in allreadyaccepted:
                        for j in don:
                            if i.donor.donor_id != j.donor_id:
                                obj=Donor.objects.get(donor_id=j.donor_id)
                                temp.append(obj)
                    return render(request,'potentialDonor.html',{'other_donors':temp,'hos':hos})     
                return render(request,'potentialDonor.html',{'other_donors':don,'hos':hos})

            if query is not None:
                lookups= Q(donor_organ__icontains=query)
                results= Donor.objects.filter(lookups).distinct()
                source_hos=Hospital.objects.get(hospital_email=loggedin_user)
                class key:  
                    def __init__(self, donor, donor_distance):  
                        self.donor = donor  
                        self.donor_distance = donor_distance
                distance=[]
                for result in results:
                    destination_hos=Hospital.objects.get(hospital_email=result.hospital_email)
                    point_destination_hos=(destination_hos.hospital_latitude, destination_hos.hospital_longitude)
                    point_source_hos=(source_hos.hospital_latitude, source_hos.hospital_longitude)

                    dis=geopy_distance(point_source_hos, point_destination_hos).km
                    distance.append( key(result, dis) ) 
                distance.sort(key=lambda x: x.donor_distance)
                final_result=[]
                for i in distance:
                    final_result.append(i.donor)



                context={'results': final_result,
                        'submitbutton': submitbutton,
                        'hos':hos}
                
                return render(request, 'potentialDonor.html', context)



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
        obj = OrganRequest.objects.filter(sender=sender, reciever=reciever,donor=donor)
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
        organ_request_time=datetime.datetime.now() 
        req = OrganRequest(sender=sender, reciever=reciever,donor=donor,organ_request_time=organ_request_time)
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
        obj = OrganRequest.objects.filter(sender=sender, reciever=reciever,donor=donor)
        obj.delete()
        msg="Request Successfully Deleted"
        ChangedState = False
        hos=Hospital.objects.exclude(hospital_email=loggedin_user)
        return render(request, 'donordetails.html',{'msg':msg, 'hos':hos, 'donor':donor, 'ChangedState':ChangedState})

def ViewRequest(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user = Hospital.objects.get(hospital_email=loggedin_user) 
        allreq = OrganRequest.objects.filter(reciever=current_user,accepted=False,declined=False)
        acceptedreq=OrganRequest.objects.filter(reciever=current_user,accepted=True,declined=False)
        return render(request, 'viewrequest.html', {'allreq' : allreq,'acceptedreq':acceptedreq})

def AcceptRequest(request):
    if request.user.is_authenticated:
        getid=request.POST.get('id','')
        organ_request=OrganRequest.objects.get(req_id=getid)
        organ_request.accepted=True
        organ_request.pending=False
        organ_request.save()

        loggedin_user=request.user.username
        current_user = Hospital.objects.get(hospital_email=loggedin_user) 
        allreq = OrganRequest.objects.filter(reciever=current_user,accepted=False,declined=False)
        acceptedreq=OrganRequest.objects.filter(reciever=current_user,accepted=True,declined=False)
        return render(request, 'viewrequest.html',{'allreq' : allreq,'acceptedreq':acceptedreq})

def DeclineRequest(request):
    if request.user.is_authenticated:
        getid=request.POST.get('id','')
        organ_request=OrganRequest.objects.get(req_id=getid)
        organ_request.declined=True
        organ_request.pending=False
        organ_request.save()

        loggedin_user=request.user.username
        current_user = Hospital.objects.get(hospital_email=loggedin_user) 
        allreq = OrganRequest.objects.filter(reciever=current_user,accepted=False,declined=False)
        acceptedreq=OrganRequest.objects.filter(reciever=current_user,accepted=True,declined=False)
        return render(request, 'viewrequest.html',{'allreq' : allreq,'acceptedreq':acceptedreq})

def ViewYourSentRequest(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_user = Hospital.objects.get(hospital_email=loggedin_user)
        allreq = OrganRequest.objects.filter(sender=current_user) 
        return render(request, 'yourrequest.html', {'allreq' : allreq})

def PledgedDonorsList(request):
    if request.user.is_authenticated:
        loggedin_user=request.user.username
        current_hospital = Hospital.objects.get(hospital_email=loggedin_user)
        donor = Pledge.objects.filter(pledge_hospital=current_hospital)
        return render(request, 'pledgeddonordetails.html',{'donor' : donor})
   

def ViewTrends(request):
    getemail=request.POST.get('email','')
    print(getemail)
    hos = Hospital.objects.get(hospital_email=getemail)
    print(hos)
    trend = Transplant.objects.get(hospital=hos)
    print(trend)
    return render(request, 'viewtrends.html', {'trend': trend})


def DonationList(request):
    if request.user.is_authenticated:
        donor_name=request.POST.get('donor_name','')
        patient_name=request.POST.get('patient_name','')
        organ=request.POST.get('organ','')
        details_added_time=datetime.datetime.now()
        loggedin_user=request.user.username
        current_user=Hospital.objects.get(hospital_email=loggedin_user)
        donation=Donation(donor_name=donor_name, patient_name=patient_name,organ=organ,
        details_added_time=details_added_time, hospital=current_user)
        donation.save()  
        print("Details are saved successfully")  
        temp=Transplant.objects.filter(hospital=current_user)
        if temp.exists():
            if(organ == "kidney"):
                temp.kidney += 1
            if(organ == "liver"):
                temp.liver += 1
            if(organ == "lung"):
                temp.lung += 1
            if(organ == "heart"):
                temp.heart += 1
            if(organ == "intestine"):
                temp.intestine += 1
            if(organ == "eye"):
                temp.eye += 1
            if(organ == "skin"):
                temp.skin += 1
            temp.save()
            print("temp is stored")
        else:
            temp1 = Transplant(hospital=current_user)
            if(organ == "kidney"):
                temp1.kidney = 1
            if(organ == "liver"):
                temp1.liver = 1
            if(organ == "lung"):
                temp1.lung = 1
            if(organ == "heart"):
                temp1.heart = 1
            if(organ == "intestine"):
                temp1.intestine = 1
            if(organ == "eye"):
                temp1.eye = 1
            if(organ == "skin"):
                temp1.skin = 1
            temp1.save()
            print("temp1 is stored")
    return render(request, 'hospitalHome.html')