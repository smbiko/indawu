from django.urls import path
from . import views


app_name ='booking'
urlpatterns = [
    path('', views.customer_booking, name='booking'),
    path('display_booking', views.display_booking, name='display_booking'),
    path('edit_booking/<booking_id>/<customer_id>',
         views.edit_booking, name='edit_booking'),
    path('delete_booking/<booking_id>/<customer_id>',
         views.delete_booking, name='delete_booking'),
    path('edit_user/<user_id>',
         views.edit_user, name='edit_user'),
    path('delete_user/<user_id>',
         views.delete_user, name='delete_user'),
]
