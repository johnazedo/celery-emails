from django.shortcuts import render
from django.http import HttpResponse

from core.tasks import to_sleep

# Create your views here.

def index(request):
    to_sleep.delay(10)
    return HttpResponse("<h1>Done!</h1>")
