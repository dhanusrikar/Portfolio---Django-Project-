from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin header customization
admin.site.site_header = "Developer Srikar"
admin.site.site_title = "Welcome to Srikar's Dashboard"
admin.site.index_title = "Weclome to this Portal"

urlpatterns = [
    path('',  views.home, name='home'),
    path('about',  views.about, name='about'),
    path('projects',  views.projects, name='projects'),
    path('contact',  views.contact, name='contact')
]