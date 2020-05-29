from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from core.models import Email
from core.tasks import send_emails

# Create your views here.

def index(request):
    # send_emails.delay()
    pass
    # return HttpResponse("<h1>Done!</h1>")


class Home(CreateView):
    template_name = 'home.html'
    model = Email
    fields = ['text']

    def dispatch(self, *args, **kwargs):
        # send_emails.delay()
        return super(Home, self).dispatch(*args, **kwargs)