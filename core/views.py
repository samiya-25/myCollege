# core/views.py
from django.shortcuts import render, redirect
from .models import Facility, GalleryImage, Staff, Admission
from .forms import AdmissionForm, ContactForm

def index(request):
    facilities = Facility.objects.all().order_by('order')[:4]
    gallery = GalleryImage.objects.all()[:3]
    return render(request,'index.html', {'facilities':facilities, 'gallery':gallery})

def about(request):
    return render(request,'about.html')

def gallery(request):
    images = GalleryImage.objects.order_by('-uploaded')
    return render(request,'gallery.html', {'images':images})

def facilities_view(request):
    facilities = Facility.objects.order_by('order')
    return render(request,'facilities.html', {'facilities':facilities})

def admissionProcess(request):
    admissionData=Admission.objects.all()

    admissionData_render={
        'admission':admissionData,
    }
    return render(request,'admissions.html',admissionData_render)

def admissions(request):
    if request.method == 'POST':
        f = AdmissionForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('admissions')  # or show success message
    else:
        f = AdmissionForm()
    return render(request,'admissions.html', {'form':f})

def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('contact')
    else:
        f = ContactForm()
    return render(request,'contact.html', {'form':f})

def staff(request):
    teaching = Staff.objects.filter(staff_type=Staff.TEACHING)
    non_teaching = Staff.objects.filter(staff_type=Staff.NON_TEACHING)
    return render(request,'staff.html', {'teaching':teaching,'non_teaching':non_teaching})
