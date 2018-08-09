from rest_framework import serializers
from .models import Room


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    reservations = serializers.HyperlinkedRelatedField(many=True, view_name='reservation-detail', read_only=True)

    class Meta:
        model = Room
        fields = '__all__'
