from django.shortcuts import render, HttpResponse
from .models import Service
# Create your views here.

def home(request):
    sers = Service.objects.all()

    context = {
        'sers': sers
    }


    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')



def blog(request):
    return render(request, 'main/blog.html')


def blogdetails(request):
    return render(request, 'main/blog-details.html')


def projects(request):
    return render(request, 'main/projects.html')


def project_details(request):
    return render(request, 'main/project-details.html')


def services(request):
    return render(request, 'main/services.html')


def service_details(request):
    return render(request, 'main/service-details.html')


