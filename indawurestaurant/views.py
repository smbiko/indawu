from django.contrib import admin
from django.urls import path, include
from home import views 
from django.conf import settings 
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('bookings/', include('booking.urls'), name='booking_urls'),

]

