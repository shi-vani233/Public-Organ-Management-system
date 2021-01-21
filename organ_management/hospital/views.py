from django.shortcuts import render

def Mainpage(request):
    return render(request, 'main.html', context=None)

def DonorList(request):
    return render(request, 'donorList.html', context=None)

def PotentialDonorList(request):
    return render(request, 'potentialDonor.html', context=None)

def Login(request):
    return render(request, 'login.html', context=None)

def hospitalHome(request):
    return render(request, 'hospitalHome.html', context=None)



# Create your views here.
