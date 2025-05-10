from django.shortcuts import render, reverse
from django.shortcuts import render, get_object_or_404, reverse
from home.models import Contact
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request, 'index.html')

def contact_us(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')


