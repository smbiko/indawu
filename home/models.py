from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


BOOKING_STATUS = ((0, 'requested'), (1, 'Confirmed'), (2, 'Declined'))


class Contact(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}, {self.email}" 

    class Meta:
        verbose_name_plural = "Contact Table"  



class Customer(models.Model):
    featured_image = CloudinaryField('image', default='placeholder')
    full_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='home_customers')


    def __str__(self):
        return f"{self.user}"


class Booking(models.Model):
    """
    Model for Booking
    """
    featured_image = CloudinaryField('image', default='placeholder')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_accompanying = models.IntegerField(default=1)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Booking by {self.customer}"