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
import random2


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#def home(request):
#    signs = Roadsign.objects.filter()
#    context = {
 #       "signs": signs,
  #  }
  #  return render(request, "signs.html", context)

def home(request):
    count_signs = Roadsign.objects.filter().count()
    n = random2.randint(1,count_signs)
    random = Roadsign.objects.filter(pk=n)
    context = {
        "signs": random,
    }
    return render(request, "signs.html", context)