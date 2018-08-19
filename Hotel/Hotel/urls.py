"""Hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from rest_framework import routers
from reservation import views as reservationviews
from room import views as roomviews
from user import views as userviews
from django.urls import path


router = routers.DefaultRouter()
router.register(r'reservation', reservationviews.ReservationViewSet, base_name='reservation')
router.register(r'room', roomviews.RoomViewSet)
router.register(r'user', userviews.UserViewSet, base_name='user')
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-auth/')
    path('AvalibleDates', roomviews.AvailableDatesView.as_view()),
]
