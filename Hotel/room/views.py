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
        for room in Room.objects.all():
            for reservation in room.reservations:
                pass
        unavaliblerooms = Reservation.objects.filter(start_date__range=[start_date, end_date],
                                                         end_date__range=[start_date, end_date]).values('res_room')
        queryset = queryset.filter().exclude(id__in=unavaliblerooms)

        return queryset
