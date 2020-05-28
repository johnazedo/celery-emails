from django.shortcuts import render
from django.http import HttpResponse

from core.tasks import send_emails

# Create your views here.

def index(request):
    send_emails.delay()
    return HttpResponse("<h1>Done!</h1>")
