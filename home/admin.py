from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class Contact(admin.ModelAdmin):
    """
    Set displays for Contact Form Submissions on the admin panel
    """
    list_display = ("name", "email", "date_posted")
    search_fields = ("name",)
