from django.contrib import admin
from .models import Contact

admin.site.site_header = "Indawu | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email',]



admin.site.register(Contact, ContactAdmin)