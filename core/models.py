# core/models.py
from django.db import models

class BasePage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(blank=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Facility(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='facilities/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    def __str__(self): return self.name

class GalleryImage(models.Model):
    caption = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=50, choices=[
        ('events','Events'),('sports','Sports'),('classroom','Classroom'),('students','Students')
    ], default='events')
    uploaded = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.caption or f"Image {self.id}"

class Staff(models.Model):
    TEACHING = 'teaching'
    NON_TEACHING = 'non-teaching'
    TYPE_CHOICES = [(TEACHING,'Teaching'),(NON_TEACHING,'Non Teaching')]
    name = models.CharField(max_length=150)
    role = models.CharField(max_length=120)
    staff_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=TEACHING)
    photo = models.ImageField(upload_to='staff/', blank=True, null=True)
    bio = models.TextField(blank=True)
    def __str__(self): return self.name

class AdmissionInquiry(models.Model):
    name = models.CharField(max_length=150)
    parent_name = models.CharField(max_length=150, blank=True)
    mobile = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    class_applied = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"{self.name} - {self.mobile}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Msg from {self.name}"
