from django.shortcuts import render, HttpResponse, redirect
from .models import Service, Construction, Project, Blog, Contact, GUsers
from .forms import ContactForm
from guest_user.decorators import allow_guest_user
# Create your views here.

@allow_guest_user
def home(request):
    user = request.user.username
    try:
        u = GUsers(username=user)
        u.save()
    except:
        pass

    sers = Service.objects.all()
    cons = Construction.objects.all()
    pros = Project.objects.all()
    blogs = Blog.objects.all()

    if request.method == 'POST':
        ism = request.POST.get('ism')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('xabar')
        con = Contact(name=ism, email=email, subject=phone, message=message)
        con.save()
        return redirect('home')


    context = {
        'sers': sers,
        'cons': cons,
        'pros': pros,
        'blogs': blogs
    }


    return render(request, 'main/index.html', context)

def about(request):
    # CREATE
    # serv = Service(title='Test uchun title', body='Test uchun body', icon='Test uchun icon')
    # serv.save()
    # READ
    # serv = Service.objects.all()
    # UPDATE
    # serv = Service.objects.get(pk=3)
    # serv.title = "O'zgartirilgan title"
    # serv.icon = 'Test icon'
    # serv.save()
    # DELETE
    # serv = Service.objects.get(pk=6)
    # serv.delete()


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


