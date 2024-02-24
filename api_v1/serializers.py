from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import *


class HousingComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousingComplex
        fields = ('pk', 'name', 'office', 'street')


class HouseSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = House
        fields = ('pk', 'address')

    def get_address(self, obj):
        return obj.address.short_str()


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'