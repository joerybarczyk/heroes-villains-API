from rest_framework import serializers
from .models import *

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id','name','alter_ego','powers','catchphrase', 'super_type','super_type_id']
        depth = 1

    super_type_id = serializers.IntegerField(write_only=True)

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = ['id', 'name']