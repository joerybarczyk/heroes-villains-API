from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Super
from .serializers import SuperSerializer

# Create your views here.
class SuperList(APIView):
    def get(self, request):
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)

class SuperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer