from django import forms
from django.forms.widgets import DateInput, TimeInput
from .models import Customer, Booking, User

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
            'booking_date': DateInput(attrs={'id': 'datepicker',
                                             'autocomplete': 'off'}),
            'booking_time': TimeInput(attrs={'id': 'timepicker',
                                             'autocomplete': 'off'})
        }


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'email')