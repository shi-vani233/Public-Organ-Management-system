from django.shortcuts import render

# Create your views here.
def BloodDonationHome(request):
    return render(request, 'BloodDonation.html', context=None)

def Volunteer(request):
    return render(request, 'volunteer.html', context=None)