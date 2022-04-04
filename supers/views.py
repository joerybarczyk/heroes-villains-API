from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class SuperList(APIView):

    def get(self, request):
        queryset = Super.objects.all()
        type = self.request.query_params.get('type')
        hero = self.request.query_params.get('hero')
        villain = self.request.query_params.get('villain')

        if type:
            type_filtered_queryset = queryset.filter(super_type__type = type)
            serializer = SuperSerializer(type_filtered_queryset, many=True)
            return Response(serializer.data)

        if hero and villain:
            return(self.compare_hero_and_villain())

        return Response(self.heroes_and_villains_response())

    def post(self, request):
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def heroes_and_villains_response(self):
        supers = Super.objects.all()
        heroes = supers.filter(super_type__type = 'hero')
        villains = supers.filter(super_type__type = 'villain')

        custom_response = {'heroes': [], 'villains': []}

        custom_response['heroes'] = SuperSerializer(heroes, many=True).data
        custom_response['villains'] = SuperSerializer(villains, many=True).data

        return custom_response

    def compare_hero_and_villain(self, hero_value, villain_value):
        hero = Super.objects.get(name=hero_value)
        villain = Super.objects.get(name=villain_value)

        

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