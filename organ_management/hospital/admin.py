from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'username', 'email']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'username','display_name', 'address1', 'address2', 'zip_code', 'city', 'mobile_phone', 'photo',)}),
    ) 
    fieldsets = UserAdmin.fieldsets + (
       (None, {'fields': ('display_name', 'address1', 'address2', 'zip_code', 'city', 'mobile_phone', 'photo',)}),
) 
    
    

admin.site.register(CustomUser, CustomUserAdmin)

