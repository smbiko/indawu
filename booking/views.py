from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Sum
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Booking, Customer
from .forms import CustomerForm, BookingForm, UserForm


def limit_no_persons(date, time, accompanying):

    persons_limit = False
    unavailable = Booking.objects.filter(booking_status=1,
                                         booking_date=date, booking_time=time)
    total_persons = unavailable.aggregate(Sum('number_accompanying'))[
        'number_accompanying__sum']
    if total_persons is None:
        total_persons = 0
    if total_persons + accompanying <= 10:
        persons_limit = True
    else:
        persons_limit = False
    return persons_limit


def unavailable_dates():
    """
      the function executes the action when the restaurant is fully booked with confirmed bookings
      for that particular date/time
    """
    confirmed_bookings = Booking.objects.filter(booking_status=1)
    bookings_max_persons = confirmed_bookings.values(
        'booking_date').annotate(
            persons=Sum('number_accompanying')).filter(persons=200)
    unavailable_dates = [booking['booking_date']
                         for booking in bookings_max_persons]
    return unavailable_dates


def check_availability(date, time):
    
    unavailable = Booking.objects.filter(
        booking_date=date, booking_time=time, booking_status=1)
    available = True
    total_persons = unavailable.aggregate(Sum('number_accompanying'))[
        'number_accompanying__sum']
    if unavailable.exists() and total_persons >= 10:
        available = False
    else:
        available = True
    return available


def customer_booking(request):
    
    unavailable_booking_dates = []
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST, prefix='customer')
        booking_form = BookingForm(request.POST, prefix='booking')
        if customer_form.is_valid() and booking_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.user = request.user
            customer.save()
            booking = booking_form.save(commit=False)
            booking.customer = customer
            if check_availability(booking.booking_date,
                                  booking.booking_time) and limit_no_persons(
                                    booking.booking_date, booking.booking_time,
                                    booking.number_accompanying):
                booking.save()
                customer_form = CustomerForm()
                booking_form = BookingForm()
                messages.add_message(request, messages.SUCCESS,
                                     'Your booking request is accepted!')
                return redirect('display_booking')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Please look for another Date and Time!')
    else:
        customer_form = CustomerForm(prefix='customer')
        booking_form = BookingForm(prefix='booking')
        unavailable_booking_dates = unavailable_dates()

    context = {
        'customer_form': customer_form,
        'booking_form': booking_form,
        'unavailable_dates': unavailable_booking_dates,
    }

    return render(request, 'booking.html', context)


def display_booking(request):
    """
    came from: https://www.w3schools.com/django/django_queryset_filter.php
    """
    customer = Customer.objects.filter(user=request.user)
    bookings = Booking.objects.filter(customer__in=customer)
    context = {
        'bookings': bookings,
    }
    return render(request, 'profile.html', context)


def edit_booking(request, booking_id, customer_id):
    """
    Edit booking function will display a pre filled form for a
    specific booking of the users choosing and allows this booking
    to be edited.
    """
    unavailable_booking_dates = []
    booking = get_object_or_404(Booking, id=booking_id)
    customer = get_object_or_404(Customer, id=customer_id)
    if not customer.user == request.user:
        messages.error(request,
                       'Error, you are unauthorized to edit this booking')
        return redirect(reverse('home'))
    else:
        if request.method == "POST":
            booking_form = BookingForm(request.POST, instance=booking)
            customer_form = CustomerForm(request.POST, instance=customer)
            if customer_form.is_valid() and booking_form.is_valid():
                customer_form.save()
                booking = booking_form.save(commit=False)
                booking.customer = customer
                if check_availability(booking.booking_date,
                                      booking.booking_time) and limit_no_persons(
                                      booking.booking_date, booking.booking_time,
                                      booking.number_accompanying):
                    booking_form.save()
                    return redirect('display_booking')
                else:
                    messages.add_message(request, messages.ERROR,
                                         'Requested Date and time unavailable!')
        booking_form = BookingForm(instance=booking)
        customer_form = CustomerForm(instance=customer)
        unavailable_booking_dates = unavailable_dates()
        context = {
            'booking_form': booking_form,
            'customer_form': customer_form,
            'unavailable_dates': unavailable_booking_dates,
        }
        return render(request, 'edit_booking.html', context)


def delete_booking(request, booking_id, customer_id):
    """
    Delete booking will delete a specific booking of a users choosing.
    A message is displayed to user once booking has been deleted.
    This function redirects to display booking.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    customer = get_object_or_404(Customer, id=customer_id)
    booking.delete()
    customer.delete()
    messages.add_message(request, messages.WARNING,
                         'Booking has been deleted!')
    return redirect('display_booking')


def edit_user(request, user_id):
    """
    Edit user allows the user to edit their username and email.
    """
    user = get_object_or_404(User, id=user_id)
    if not user == request.user:
        messages.error(request,
                       'Error you are unauthorized to edit this users account')
        return redirect(reverse('home'))
    else:
        if request.method == "POST":
            form = UserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('display_booking')
        form = UserForm(instance=user)
        context = {
            'form': form,
        }
        return render(request, 'edit_user.html', context)


def delete_user(request, user_id):
    """
    Delete user will delete a users account. A message is displayed to the user
    if deletion is successful.
    """
    user = get_object_or_404(User, id=user_id)
    user.delete()
    messages.add_message(request, messages.WARNING,
                         'Your account has been deleted!')
    return redirect('home')