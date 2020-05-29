from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView
from core.models import Email
from django.urls import reverse_lazy

# Create your views here.
class Home(SuccessMessageMixin,CreateView):
    template_name = 'home.html'
    model = Email
    fields = ['text']
    success_url = reverse_lazy('core:home')
    success_message = "%(text)s has been added!"

    def dispatch(self, *args, **kwargs):
        # send_emails.delay()
        return super(Home, self).dispatch(*args, **kwargs)
