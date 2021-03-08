from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import distance as geopy_distance
from hospital.models import Hospital
from home.models import Pledge

def Homepage(request):
    hos = Hospital.objects.all()
    print("YASH GANDO 6 BAUJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
    return render(request, 'home.html', {'hos':hos})

def DonorPledge(request):
    pledge_name=request.POST.get('pledge_name','')
    pledge_city=request.POST.get('pledge_city','')
    pledge_hospital = request.POST.get('pledge_hospital','')
    pledge_mobile_no=request.POST.get('pledge_mobile_no','')
    pledge_bloodGroup=request.POST.get('pledge_bloodGroup','')
    pledge_gender=request.POST.get('pledge_gender','')
    pledge_info=request.POST.get('pledge_info','')
    pledge_diseases=request.POST.get('pledge_diseases','')
    pledge_addiction=request.POST.getlist('pledge_addiction','')
    pledge_organ=request.POST.get('pledge_organ','')  
    print(pledge_hospital)
    print(pledge_diseases)
    current_hos = Hospital.objects.get(hospital_email=pledge_hospital)
    hos = Hospital.objects.all() 
    if len(pledge_mobile_no)!=10:
        msg_phone="phone number must be of length 10, please fill the form again with correct contact no"
    else:
        msg_phone=''
    if not ( msg_phone):
        donor=Pledge(pledge_name=pledge_name,pledge_city=pledge_city, pledge_mobile_no=pledge_mobile_no,  pledge_organ = pledge_organ,
        pledge_bloodGroup=pledge_bloodGroup,pledge_gender=pledge_gender, pledge_diseases=pledge_diseases, pledge_addiction=pledge_addiction,
        pledge_info=pledge_info, pledge_hospital=current_hos)
        donor.save()
        msg="You are registered!"
        return render(request,'home.html',{'msg':msg, 'hos':hos})
    else:
        return render(request ,'home.html',{'msg_phone':msg_phone, 'hos':hos})


 