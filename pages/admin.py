from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_display_links = ['name', 'email']
    search_fields = ['name', 'email', 'message']
    list_filter = ['created_at']

@admin.register(BannerModel)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'collection', 'is_active']
    list_display_links = ['title', 'collection', 'is_active']
    search_fields = ['title', 'collection',]
    list_filter = ['created_at']