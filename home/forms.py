
from .models import Contact
from django import forms
from django.forms.widgets import DateInput, TimeInput
from .models import Customer, Booking, User

from http import HTTPStatus


class ContactForm(forms.ModelForm):
    """
    Contact Form
    """

    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20}))

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "message",
        )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        message = cleaned_data.get("message")
        return cleaned_data


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