from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ReservationSerializer, UserSerializer
from .models import Reservation
from rest_framework import permissions


# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservations to be viewed or edited.
    """
    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Reservation.objects.all()
        else:
            queryset = Reservation.objects.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




