from django.db import models


class Person(models.Model):
    """
    Personne physique lors d'un voyage.
    """
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    birthday = models.DateField()


class Booking(models.Model):
    """
    Modèle pour gérer les réservations.
    """
    # - client
    # - réservations de vols
    # - réservations d'hotels
    # - Est confirmée