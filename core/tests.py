from django.test import TestCase
from django.test import Client
from django.urls import reverse, resolve
from core.views import Home
from core.models import Email

# Create your tests here.
class HomePageTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('core:home')
        self.template = 'home.html'
    
    def test_home_url(self):
        self.assertEquals(resolve(self.url).func.view_class, Home)
    
    def test_home_view(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, self.template)
    
    def test_home_add_email(self):
        response = self.client.post(self.url, {
            'text':'email.example@gmail.com'
        })

        email = Email.objects.get(id=1)        
        self.assertEquals(response.status_code, 302)
        self.assertEquals(email.text, 'email.example@gmail.com')

        

    


