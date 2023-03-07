from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),  # yangilik.uz/about
    path('contact', contact, name='contact'),
    path('blog', blog, name='blog'),
    path('blog-details/<int:pk>', blogdetails, name='blogdetails'),
    path('projects', projects, name='projects'),
    path('project-details', project_details, name='projectdetails'),
    path('services', services, name='services'),
    path('service-details', service_details, name='servicedetails'),

]