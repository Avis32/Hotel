from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Reservation
        # field = ('id',
        #          'url',
        #          'created',
        #          'owner',
        #          'res_room',
        #          'start_date',
        #          'end_date',
        #
        #          )
        fields = '__all__'

    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError('start_date is after end_date')
        for res in Reservation.objects.all():
            if res.res_room == attrs['res_room']:
                if res.start_date <= attrs['end_date']:
                    if res.start_date >= attrs['start_date']:
                        raise serializers.ValidationError('room is not available in selected period')
            if res.start_date <= attrs['start_date']:
                if res.end_date >= attrs['start_date']:
                    raise serializers.ValidationError('room is not available in selected period')

        return attrs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reservations = serializers.HyperlinkedRelatedField(many=True, view_name='reservation-detail', read_only=True)

    class Meta:
        model = User
        fields = '__all__'
