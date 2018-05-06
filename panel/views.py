from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lazysignup.decorators import allow_lazy_user
from django.http import HttpResponse
from django.contrib.auth import login


# Create your views here.
def home(request):
    return render(request, 'panel/home.html')


