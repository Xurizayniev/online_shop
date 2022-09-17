from django.contrib import admin
from .models import *

@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','user']
    readonly_fields = ['user', 'id', 'address2', 'address1', 'phone', 'region', 'zip_code', 'country', 'first_name', 'last_name', 'city', 'email']

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['phone_number']
    list_display_links = ['phone_number']