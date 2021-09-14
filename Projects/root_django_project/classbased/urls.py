
from django.urls import path 
from  .views import (FirstTemplate, FirstTemplateRedirect,
 FirstView)


app_name = 'classbased'
urlpatterns = [
    # we should call as_view() mwthod
    path('first/', FirstView.as_view()) ,

    # for firstTemplate
    path('template/', FirstTemplate.as_view()),

    #redirect url 
    path('template1/', FirstTemplateRedirect.as_view()),
    path('template2/', FirstTemplateRedirect.as_view()),
    path('template3/', FirstTemplateRedirect.as_view()),
    path('template4/', FirstTemplateRedirect.as_view()),



]