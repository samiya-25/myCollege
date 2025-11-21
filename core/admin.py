# core/admin.py
from django.contrib import admin
from .models import Facility, GalleryImage, Staff, AdmissionInquiry, ContactMessage

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('name','order')

@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('caption','category','uploaded')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name','role','staff_type')

@admin.register(AdmissionInquiry)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','class_applied','created')

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created')
