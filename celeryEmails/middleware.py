from django.http.response import HttpResponse
from core.views import Home

class AddEmailMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.view_class == Home:
            print(f'debug -> view_class is Home')

            # POST is being called here to create a new e-mail!
            if request.method == 'POST':
                print(f'debug -> request method is POST')
            
            # GET is being called here to send the Home Page of the site!
            if request.method == 'GET':
                print(f'debug -> request method is GET')