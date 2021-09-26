
from django.urls import path
from  .views import add_two_numbers, add_two_numbers_in_rest, info_view

from .class_views import InfoClassBasedViews
from .generic_views import(InfoModelCreateAPIView, InfoModelListAPIView,
InfoModelDestroyAPIView, InfoModelUpdateAPIView, InfoModelRetrieveAPIView)

from .viewset_views import InfoModelViewSet
from rest_framework.routers import DefaultRouter

# This will be default routing method
# now this will work with all methods get,post,patch,delete,reterieve
# with single url api modelview set
r = DefaultRouter()
r.register('info/view-set', InfoModelViewSet)

app_name = "rest"
urlpatterns = [
    path('add/', add_two_numbers),
    path('v2/add/', add_two_numbers_in_rest),
    path('info/', info_view),
    path('info/<int:pk>/', info_view),

    #rest/
    path('info/class-based/', InfoClassBasedViews.as_view()),
    path('info/generic/create/', InfoModelCreateAPIView.as_view()),
    path('info/generic/list/', InfoModelListAPIView.as_view()),
    path('info/generic/delete/<int:pk>/', InfoModelDestroyAPIView.as_view()),
    path('info/generic/update/<int:pk>/', InfoModelUpdateAPIView.as_view()),
    path('info/generic/detail/<int:pk>/', InfoModelRetrieveAPIView.as_view()),

    # for modelview single url will work for all
    # allow the actions in .as_view arguments
    # path('info/view-set/', InfoModelViewSet.as_view(actions={'get': 'list', 'post': 'create'})),
 ] + r.urls

# for more shortcut methods action={}
# we use routing method 
