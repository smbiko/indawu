from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm
from home import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('home.urls')),
    #path('', views.index, name="index"),
    #path('bookings/', include('booking.urls')),
]

def index(request):
    """
    Home Page
    """
    return render(request, "index.html")


