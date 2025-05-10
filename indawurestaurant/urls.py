from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('', include('home.urls'), name='home_urls'),
    path("accounts/", include("allauth.urls")),
    path('bookings/', include('booking.urls'), name='booking_urls'),
]
