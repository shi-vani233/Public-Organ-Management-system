from django.shortcuts import render

def Homepage(request):
    return render(request, 'home.html', context=None)

def Volunteer(request):
    return render(request, 'volunteer.html', context=None)
# Create your views here.
