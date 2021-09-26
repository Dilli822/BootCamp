
from rest_framework.viewsets import ModelViewSet
from .serializers import InfoModelSerializer
from .models import Info

# with modelview set we can  make single file api views for collective works
class InfoModelViewSet(ModelViewSet):
    serializer_class = InfoModelSerializer 
    queryset = Info.objects.all()

