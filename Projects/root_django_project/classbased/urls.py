
from django.urls import path 
from  .views import FirstTemplate, FirstView


app_name = 'classbased'
urlpatterns = [
    # we should call as_view() mwthod
    path('first/', FirstView.as_view()) ,

    # for firstTemplate
    path('template/', FirstTemplate.as_view()),

]