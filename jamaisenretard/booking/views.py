from django.views.generic import TemplateView

from rest_framework import viewsets

from jamaisenretard.booking.models import Person, ClientAccount, HotelBooking, FlyBooking, Booking
from jamaisenretard.booking.serializers import PersonSerializer, ClientAccountSerializer, HotelBookingSerializer, \
    FlyBookingSerializer, BookingSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows person to be viewed or edited.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ClientAccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows client account to be viewed or edited.
    """
    queryset = ClientAccount.objects.all()
    serializer_class = ClientAccountSerializer


class HotelBookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hotel booking to be viewed or edited.
    """
    queryset = HotelBooking.objects.all()
    serializer_class = HotelBookingSerializer


class FlyBookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows fly booking to be viewed or edited.
    """
    queryset = FlyBooking.objects.all()
    serializer_class = FlyBookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows booking to be viewed or edited.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer