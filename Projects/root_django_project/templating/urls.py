
from django.urls import path
from .views import hello_template

urlpatterns = [ 

    # templates/hello
    path('hello/', hello_template),
]