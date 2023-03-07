from django.contrib import admin
from .models import Service, Construction, DataGallery, Project, Blog, Contact
# Register your models here.


admin.site.register(Service)

admin.site.register(Construction)


admin.site.register(DataGallery)
admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Contact)