
from django.utils import timezone
from rest_framework.views import APIView 
from .models import Info
from rest_framework.response import Response
from .serializers import InfoSerializer, InfoModelSerializer
from rest_framework import status

class InfoClassBasedViews(APIView):

    def get(self, request, *args, **kwargs):
        qs = Info.objects.all()
        serializer = InfoSerializer(instance=qs, many=True)
        return Response(serializer.data)

    
    def post(self, request, *args, **kwargs):
        current_time =  timezone.now()
        print("current time is--->", current_time)
        context = {
            "current_time": current_time
        }
        # serializer = InfoSerializer(data=request.data, context=context)
        serializer = InfoModelSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response({'status': 'ok from patch method!', 'result': serializer.data}, status=201)
        return Response({'status': 'ok from patch method!', 'result': serializer.data},
                          status=status.HTTP_201_CREATED)
        



