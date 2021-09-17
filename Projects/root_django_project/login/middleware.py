
# from django.shortcuts import redirect

# from login.views import open

# # making custom middleware
# class MyCustomMiddleware:
#     #must have second argu get_reponse by docs
#     # int called only once
#     def __init__(self, get_response):
#         self.get_response = get_response

    

#     # call method gets frequently called
#     def __call__(self, request):
#         response = self.get_response(request)
#         return response

    
#     # checking the user's existance
#     # process_view called before going to the views
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         if request.login:
#             if not request.login.is_authenicated and view_func == open:
#                 return redirect('login')


