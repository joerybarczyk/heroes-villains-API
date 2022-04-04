from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class SuperList(APIView):

    def get(self, request):
        queryset = Super.objects.all()
        type = self.request.query_params.get('type')

        if type:
            type_filtered_queryset = queryset.filter(super_type__type = type)
            serializer = SuperSerializer(type_filtered_queryset, many=True)
            return Response(serializer.data)

        custom_response = {'heroes': [], 'villains': []}

        heroes = queryset.filter(super_type__type = 'hero')
        villains = queryset.filter(super_type__type = 'villain')

        custom_response['heroes'] = SuperSerializer(heroes, many=True).data
        custom_response['villains'] = SuperSerializer(villains, many=True).data
        
        return Response(custom_response)

    def post(self, request):
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SuperDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Super.objects.all()
    serializer_class = SuperSerializer

class UpdatePowers(APIView):

    def patch(self, request, pk, power_name):
        super = Super.objects.get(pk=pk)
        new_power = Power.objects.get(name=power_name)
        super.powers.add(new_power)
        serializer = SuperSerializer(super)
        return Response(serializer.data)