from rest_framework import serializers

from .models import Outlet

class OutletSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Outlet
        fields = ('name', 'address', 'open_hr', 'lat', 'long', 'waze')