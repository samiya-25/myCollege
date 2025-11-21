# schoolsite/urls.py
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('facilities/', views.facilities_view, name='facilities'),
    path('admissions/', views.admissions, name='admissions'),
    path('contact/', views.contact, name='contact'),
    path('staff/', views.staff, name='staff'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
