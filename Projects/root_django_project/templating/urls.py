
from django.urls import path
from .views import hello_render, hello_template

urlpatterns = [ 

    # templates/hello
    path('hello/', hello_template),
    
    path('hello_render/', hello_render)
]