from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import ContactForm


def home(request):
    """
    Home Page
    """
    return render(request, "index.html")


def contact(request):
    """
    Contact Page and Form
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("thank-you"))
        else:
            messages.error(
                request,
                "Failed to send message. Please try again. All fields are required.",    
            )
    form = ContactForm()
    context = {"form": form}
    return render(request, "contact.html", context)        