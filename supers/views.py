from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class SuperList(APIView):

    def get(self, request):
        queryset = Super.objects.all()

        super_type = self.request.query_params.get('type')
        hero_name = self.request.query_params.get('hero')
        villain_name = self.request.query_params.get('villain')

        if super_type:
            type_filtered_queryset = queryset.filter(super_type__type = super_type)
            serializer = SuperSerializer(type_filtered_queryset, many=True)
            return Response(serializer.data)

        if hero_name and villain_name:
            return Response(self.compare_supers(hero_name, villain_name))

        return Response(self.grouped_supers_response())

    def post(self, request):
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def compare_supers(self, super1_name, super2_name):
        '''Compare supers by their number of powers and return response containing winner and loser info'''
        super1_powers_count = len(self.get_super_powers_list(super1_name))
        super2_powers_count = len(self.get_super_powers_list(super2_name))

        if super1_powers_count > super2_powers_count:
            return self.winner_loser_response(super1_name, super2_name)
        elif super1_powers_count < super2_powers_count:
            return self.winner_loser_response(super2_name, super1_name)
        return "It's a tie! Both supers have the same number of powers"

    def get_super_powers_list(self, super_name):
        '''Get list of a super's powers'''
        super_obj = Super.objects.get(name = super_name)
        super_details = SuperSerializer(super_obj).data
        powers = super_details['powers']
        return powers

    def grouped_supers_response(self):
        '''Group supers by heroes and villains'''
        supers = Super.objects.all()
        heroes = supers.filter(super_type__type = 'hero')
        villains = supers.filter(super_type__type = 'villain')

        grouped_response = {'heroes': [], 'villains': []}

        grouped_response['heroes'] = SuperSerializer(heroes, many=True).data
        grouped_response['villains'] = SuperSerializer(villains, many=True).data

        return grouped_response

    def winner_loser_response(self, winner_name, loser_name):
        '''Return super comparison response grouped by winner and loser'''
        supers = Super.objects.all()
        winner = supers.get(name = winner_name)
        loser = supers.get(name = loser_name)

        winner_loser = {'winner': None, 'loser': None}
        winner_loser['winner'] = SuperSerializer(winner).data
        winner_loser['loser'] = SuperSerializer(loser).data

        return winner_loser


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