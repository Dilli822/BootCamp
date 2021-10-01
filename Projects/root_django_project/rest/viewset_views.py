
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import InfoModelSerializer
from .models import Info
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions  import IsAuthenticated
from .permission import IsStaffUser

# with modelview set we can  make single file api views for collective works
# class InfoModelViewSet(ModelViewSet):
#     serializer_class = InfoModelSerializer 
#     queryset = Info.objects.all() 


# this will only allow to read the data
class InfoModelViewSet(ReadOnlyModelViewSet):
    serializer_class = InfoModelSerializer 
    queryset = Info.objects.all()


    # authentication_class
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # must be staff too
    permission_classes = [IsStaffUser]

    # must have is_staff token to do this
    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsStaffUser]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

#http://127.0.0.1:8000/rest/
# we can add more api url 
# HTTP 200 OK
# Allow: GET, HEAD, OPTIONS
# Content-Type: application/json
# Vary: Accept

# {
#     "info/view-set": "http://127.0.0.1:8000/rest/info/view-set/"
# }



