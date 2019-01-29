from django.db import models


class ClientAccount(models.Model):
    """
    Compte d'une personne physique.
    """
    last_name = models.CharField('Nom de famille', max_length=100)
    first_name = models.CharField('Prénom', max_length=100)
    email = models.EmailField('Courriel')
    phone = models.CharField('Numéro de téléphone', max_length=100)

    def __str__(self):
        return 'Compte de "{0} {1}"'.format(self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Compte client'
        verbose_name_plural = 'Comptes client'


class Person(models.Model):
    """
    Personne physique lors d'un voyage.
    """
    last_name = models.CharField('Nom de famille', max_length=100)
    first_name = models.CharField('Prénom', max_length=100)
    birthday = models.DateField('Date de naissance')
    client_account = models.ForeignKey(ClientAccount, verbose_name='Compte client lié', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.first_name)

    class Meta:
        verbose_name = 'Personne'
        verbose_name_plural = 'Personnes'


class Booking(models.Model):
    """
    Modèle pour gérer les réservations.
    """
    client_account = models.ForeignKey(ClientAccount, verbose_name='Compte client lié', on_delete=models.PROTECT)
    is_confirmed = models.BooleanField('Est confirmée')

    class Meta:
        verbose_name = 'Réservation'
        verbose_name_plural = 'Réservations'


class HotelBooking(models.Model):
    """
    Modèle de réservation d'hotels
    """
    booking = models.ForeignKey(Booking, verbose_name='Réservation liée', on_delete=models.CASCADE)
    name = models.CharField('Nom de l\'hotel', max_length=100)
    place = models.CharField('Lieu', max_length=100)
    arrival_date = models.DateTimeField('Date d\'arrivée')
    departure_date = models.DateTimeField('Date de départ')
    price = models.FloatField('Prix')
    is_confirmed = models.BooleanField('Est confirmée')

    class Meta:
        verbose_name = 'Réservation pour un hotel'
        verbose_name_plural = 'Réservations pour un hotel'


class FlyBooking(models.Model):
    """
    Modèle de réservation des vols
    """
    booking = models.ForeignKey(Booking, verbose_name='Réservation liée', on_delete=models.CASCADE)
    number = models.CharField('Numéro du vol', max_length=50)
    departure_date = models.DateTimeField('Date de départ')
    arrival_date = models.DateTimeField('Date d\'arrivée')
    departure_place = models.CharField('Lieu de départ', max_length=100)
    arrival_place = models.CharField('Lieu d\'arrivée', max_length=100)
    price = models.FloatField('Prix')
    is_confirmed = models.BooleanField('Est confirmée')

    class Meta:
        verbose_name = 'Réservation pour un vol'
        verbose_name_plural = 'Réservations pour un vol'
