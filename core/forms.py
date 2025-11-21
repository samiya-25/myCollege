# core/forms.py
from django import forms
from .models import AdmissionInquiry, ContactMessage

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionInquiry
        fields = ['name','parent_name','mobile','email','class_applied','message']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name','email','phone','message']
