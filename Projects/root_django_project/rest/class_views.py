
from rest_framework.views import APIView 
from .models import Info
from rest_framework.response import Response
from .serializers import InfoSerializer


class InfoClassBasedViews(APIView):

    def get(self, request, *args, **kwargs):
        qs = Info.objects.all()
        serializer = InfoSerializer(instance=qs, many=True)
        return Response(serializer.data)

    
    def post(self, request, *args, **kwargs):
        serializer = InfoSerializer(data=request.data, instance=obj)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'ok from patch method!', 'result': serializer.data})

