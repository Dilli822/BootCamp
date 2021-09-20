

from django.urls import path
from .views import StatusMessageCreateView

app_name = 'statusapp'

urlpatterns = [
    path('create/', StatusMessageCreateView.as_view(), name='create')
]