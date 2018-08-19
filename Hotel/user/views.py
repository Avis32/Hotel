from django.shortcuts import render
from rest_framework import viewsets,mixins
from .serializers import UserSerializer
from rest_framework import permissions
from django.contrib.auth.models import User
#from rest_framework.authentication import SessionAuthentication
from rest_framework import response

# Create your views here.
class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    #authentication_classes = (SessionAuthentication,)
    #permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):

        if self.request.user and self.request.user.is_staff:
            return User.objects.all()
        else:
            return []

    #def perform_create(self, serializer):
    # def create(self, request, *args, **kwargs):
    #     User.objects.create_user(request, *args, **kwargs)
    #     return



