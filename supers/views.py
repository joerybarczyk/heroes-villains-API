from rest_framework import generics, mixins
from .models import Super
from .serializers import SuperSerializer


class SuperList(generics.ListCreateAPIView):
    serializer_class = SuperSerializer

    def get_queryset(self):
        queryset = Super.objects.all()
        type = self.request.query_params.get('type')

        if type:
            queryset = queryset.filter(super_type__type = type)
            
        return queryset

class SuperDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Super.objects.all()
    serializer_class = SuperSerializer