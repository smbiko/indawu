from django.contrib import admin
from django.urls import path, include
from home import views 
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('', views.home, name='home'),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('menu/', views.menu, name='menu'),
    path("accounts/", include("allauth.urls")),
    path('booking/', include('booking.urls'), name='booking_urls'),
    #path('customer_booking/', include('booking.urls'), name='booking'),

    #path('register/',views.register,name="register"),
    #path('check_user_exists/',views.check_user_exists,name="check_user_exist"),
    #path('login/', views.signin, name='login'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    #path('logout/', views.user_logout, name='logout'),
]