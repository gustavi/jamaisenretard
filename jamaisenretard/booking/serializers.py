from rest_framework import serializers

from jamaisenretard.booking.models import Person, ClientAccount, FlyBooking, HotelBooking, Booking


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'url', 'last_name', 'first_name', 'birthday', 'client_account')


class ClientAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientAccount
        fields = ('id', 'url', 'last_name', 'first_name', 'email', 'phone', 'person_set')


class FlyBookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FlyBooking
        fields = '__all__'


class HotelBookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HotelBooking
        fields = '__all__'


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ('client_account', 'is_confirmed', 'hotelbooking_set', 'flybooking_set')
