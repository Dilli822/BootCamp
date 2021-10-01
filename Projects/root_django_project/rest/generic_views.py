

# generic view for api
# cdrf.co
# must which method/functions are calling to eachother

from rest_framework.generics import (CreateAPIView, 
ListAPIView,DestroyAPIView, UpdateAPIView, RetrieveAPIView)

from .serializers import InfoModelSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions  import IsAuthenticated

from .models import Info 
from .pagination import MyLimitOffSetPagination

# for searching & filtering 
from rest_framework.filters import SearchFilter, OrderingFilter

# for filtering only specific fileds
from django_filters.rest_framework import DjangoFilterBackend

class InfoModelCreateAPIView(CreateAPIView):
    serializer_class = InfoModelSerializer

    # for permissions and authentication 
    # writethe validations and code below
    
    def perform_create(self, serializer):
        serializer.save()
        print("Ok the serializer is saved!")

# for list api view--> listing the datas
class InfoModelListAPIView(ListAPIView):
    # querset = Info.objects.all()
    serializer_class = InfoModelSerializer

    # remeber to keep authenticate and permission class
    # to every api view 
    authentication_classes = [TokenAuthentication]
    #permission for only sign in users
    permission_classes = [IsAuthenticated ]


    #pagination
    # Limit-->5  offset--> 2(initial point)
    pagination_class = MyLimitOffSetPagination
    #filtering and searching
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]

    #arragning for which filed can be searched like name and id
    search_fields = ['name']
    order_fields = ['name', 'id']
    filterset_fields = ['name']

    # lets' filter and search filed or name directly


    def get_queryset(self):
        return Info.objects.all()


# Destroy API View
class InfoModelDestroyAPIView(DestroyAPIView):
    queryset = Info.objects.all()


# updated API View
# we have two methods PUT and PATCH method
class InfoModelUpdateAPIView(UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer


# Retrieve method
class InfoModelRetrieveAPIView(RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoModelSerializer

    



# for reterieve and update combined class view
# for that we have reteriveupdate method
# reterieve+update+destroy method 
# for more we can use mixins and customize the generic view
# for more details we can visit cdrf.co website



