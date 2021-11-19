from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
    get_list_or_404,
    HttpResponse,
    reverse,
)
from .models import Roadsign


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    signs = Roadsign.objects.filter()
    context = {
        "signs": signs,
    }
    return render(request, "signs.html", context)