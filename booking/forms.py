from django import forms
from django.forms.widgets import DateInput, TimeInput
from .models import Customer, Booking, User
from http import HTTPStatus

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('full_name', 'email', 'phone_number')


class BookingForm(forms.ModelForm):
    """
    Booking form set up. It includes the widgets for the
    datepicker and timepicker.
    """
    class Meta:
        model = Booking
        fields = ('booking_date', 'booking_time', 'number_accompanying')
        widgets = {
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Date'}),
            'booking_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'Time'}),
            'number_accompanying': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'}),
        }


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'email')
