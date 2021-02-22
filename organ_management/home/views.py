from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import distance as geopy_distance

geolocator = Nominatim(user_agent="home")
a="Piplod,surat"+" "
b="Surat"
c=a+b
location1 = geolocator.geocode(c)
location2 = geolocator.geocode("Pune")
location3 = geolocator.geocode("delhi")
def Homepage(request):
    print(location1.address)
    pointA=(location1.latitude, location1.longitude)
    print(pointA)
    print(location2.address)
    pointB=(location2.latitude, location2.longitude)
    print(pointB)
    print(location3.address)
    pointC=(location3.latitude, location3.longitude)
    print(pointC)
    d1 = geopy_distance(pointA, pointB).km
    print("vadodara to pune   ",d1)
    d2 = geopy_distance(pointA, pointC)
    print("vadodara to Delhi   ",d2)
    return render(request, 'home.html', context=None)


# Create your views here.
