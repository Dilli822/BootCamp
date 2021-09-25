

# generic view for api
# cdrf.co
# must which method/functions are calling to eachother

from rest_framework.generics import (CreateAPIView, 
ListAPIView,DestroyAPIView, UpdateAPIView, RetrieveAPIView)

from .serializers import InfoModelSerializer

from .models import Info 
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




