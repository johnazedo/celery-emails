from django.conf import settings

class HomeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     to_string = f'HomeMiddleware -> \n View Function: {view_func}\n View args: {view_args}\n View kwargs: {view_kwargs}'
        
    #     print(to_string)

class AddEmailMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # print(f'{dir(request)}')
        print(request.POST['text'])
        # to_string = f'AddEmailMiddleware -> \n View Function: {view_func}\n View args: {view_args}\n View kwargs: {view_kwargs}'
        # print(to_string)