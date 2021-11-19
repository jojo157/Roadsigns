from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request, "base.html")