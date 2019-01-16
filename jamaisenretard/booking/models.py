from django.db import models


class Person(models.Model):
    """
    Personne physique lors d'un voyage.
    """
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birthday = models.DateField()


class ClientAccount(models.Model):
    """
    Compte d'une personne physique
    """
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    persons = models.ForeignKey(Person, on_delete=models.PROTECT)


class HotelBooking(models.Model):
    """
    Modèle de réservation d'hotels
    """
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    arrival_date = models.DateTimeField()
    departure_date = models.DateTimeField()
    price = models.FloatField()
    is_confirmed = models.BooleanField()


class FlyBooking(models.Model):
    """
    Modèle de réservation des vols
    """
    number = models.CharField(max_length=50)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    departure_place = models.CharField(max_length=100)
    arrival_place = models.CharField(max_length=100)
    price = models.FloatField()
    is_confirmed = models.BooleanField()


class Booking(models.Model):
    """
    Modèle pour gérer les réservations.
    """
    client_account = models.ForeignKey(ClientAccount, on_delete=models.PROTECT)
    fly_booking = models.ForeignKey(FlyBooking, on_delete=models.PROTECT)
    hotel_booking = models.ForeignKey(HotelBooking, on_delete=models.PROTECT)
    is_confirmed = models.BooleanField()
