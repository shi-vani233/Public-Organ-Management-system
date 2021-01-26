from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserUpdateForm

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

def profile_view(request):
    return render(request, 'account/profile.html', context=None)


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm


class CustomUserDeleteView(DeleteView):
    model = CustomUser
    success_url = reverse_lazy('account_signup')

# Create your views here.
