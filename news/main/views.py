from django.shortcuts import render, HttpResponse, redirect
from .models import Service, Construction, Project, Blog
from .forms import ContactForm
# Create your views here.

def home(request):
    sers = Service.objects.all()
    cons = Construction.objects.all()
    pros = Project.objects.all()
    blogs = Blog.objects.all()

    context = {
        'sers': sers,
        'cons': cons,
        'pros': pros,
        'blogs': blogs
    }


    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')

    return render(request, 'main/contact.html')



def blog(request):
    return render(request, 'main/blog.html')


def blogdetails(request, pk):
    blog = Blog.objects.get(pk=pk)
    allblogs = Blog.objects.all()
    context = {
        'blog':blog,
        'all': allblogs
    }
    return render(request, 'main/blog-details.html', context)


def projects(request):
    return render(request, 'main/projects.html')


def project_details(request):
    return render(request, 'main/project-details.html')


def services(request):
    return render(request, 'main/services.html')


def service_details(request):
    return render(request, 'main/service-details.html')


