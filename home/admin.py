from django.contrib import admin
from .models import Contact

admin.site.site_header = "Indawu | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']

admin.site.register(Contact, ContactAdmin)