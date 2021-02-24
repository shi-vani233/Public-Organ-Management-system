from django.contrib import admin
from hospital.models import Hospital,Donor, OrganRequest, Transplant, Donation

# Register your models here.
admin.site.register(Hospital) 
admin.site.register(Donor)
admin.site.register(OrganRequest)
admin.site.register(Transplant)
admin.site.register(Donation)