from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

BOOKING_STATUS = ((0, 'requested'), (1, 'Confirmed'), (2, 'Declined'))




class Customer(models.Model):
    
    full_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking_customers', null=True, blank=True )


    def __str__(self):
        return f"{self.user}"


class Booking(models.Model):
    """
    Model for Booking
    """
    full_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=20, default='0000000000' )
    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_accompanying = models.IntegerField(default=1)
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Booking by {self.customer}"

        
