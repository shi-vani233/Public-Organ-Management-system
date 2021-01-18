from django.shortcuts import render

def Homepage(request):
    return render(request, 'home.html', context=None)
# Create your views here.
