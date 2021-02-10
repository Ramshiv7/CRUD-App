from django.shortcuts import render,redirect
import requests, json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .forms import RegisterForm

# Create your views here.

def home(request):
    return render(request, 'html-static/index.html')


def register(response):

    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/activity")

    else:
        form = RegisterForm()

    return render(response, 'html-static/register.html', {'form': form})


def activity(request):
    return render(request, 'html-static/activities_home.html')
