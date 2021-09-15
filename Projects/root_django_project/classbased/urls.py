
from classbased.crud_views import Create, List, Detail, Update, Delete
from django.urls import path 
from  .views import FirstTemplate, FirstTemplateRedirect,FirstView


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

    # path for form create
    # we must call .as_view() for generic class view
    # urls be /c/create/
    path('create/', Create.as_view(), name='create'),

    # URL for list model
    path('list/', List.as_view(), name= 'list'),

    # for detail with id
    path('detail/<int:id>/', Detail.as_view(),name='detail'),
    
    # for pk itself
    # path('detail/<int:pk>/',Detail.as_view(),name='detail'),

    # for update
    path('update/<int:id>/', Update.as_view(),name='update'),

    # for delete with default pk
    path('delete/<int:id>/', Delete.as_view(), name='Delete')
]