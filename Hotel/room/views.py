from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Room
from reservation.models import Reservation
from .serializers import RoomSerializer
from rest_framework import permissions
import datetime
# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAdminUser, )

class AvailableDatesView(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get_queryset(self):
        start_date = self.request.query_params.get('from', datetime.date.today()+datetime.timedelta(days=1))
        end_date = self.request.query_params.get('to', datetime.date.today()+datetime.timedelta(days=2))
        if type(start_date) == str:
            start_date = start_date.split('-')
            start_date = datetime.date(year=int(start_date[0]), month=int(start_date[1]), day=int(start_date[2]))
        if type(end_date) == str:
            end_date = end_date.split('-')
            end_date = datetime.date(year=int(end_date[0]), month=int(end_date[1]), day=int(end_date[2]))

        unavaliblerooms = []
        for reservation in Reservation.objects.all():
            if reservation.start_date <= end_date:
                if reservation.start_date >= start_date:
                    unavaliblerooms.append(reservation.res_room.id)
                if reservation.start_date >= start_date:
                    if reservation.start_date <= end_date:
                        unavaliblerooms.append(reservation.res_room.id)
        queryset = Room.objects.all().filter().exclude(id__in=unavaliblerooms)

        return queryset
