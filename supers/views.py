from rest_framework import generics
from .models import Super
from .serializers import SuperSerializer

# Create your views here.
class SuperList(generics.ListCreateAPIView):
    pass

class SuperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer