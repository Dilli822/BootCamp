
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import InfoModelSerializer
from .models import Info

# with modelview set we can  make single file api views for collective works
# class InfoModelViewSet(ModelViewSet):
#     serializer_class = InfoModelSerializer 
#     queryset = Info.objects.all() 


# this will only allow to read the data
class InfoModelViewSet(ReadOnlyModelViewSet):
    serializer_class = InfoModelSerializer 
    queryset = Info.objects.all()

    # we can override any method like list for get,post request method

    # feature on sending email for user creation
    # def create(self):
    #     send_email()
    #     super.create() 

#http://127.0.0.1:8000/rest/
# we can add more api url 
# HTTP 200 OK
# Allow: GET, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept

# {
#     "info/view-set": "http://127.0.0.1:8000/rest/info/view-set/"
# }



