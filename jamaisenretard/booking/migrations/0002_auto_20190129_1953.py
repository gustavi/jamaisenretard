# Generated by Django 2.1.5 on 2019-01-29 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Réservation', 'verbose_name_plural': 'Réservations'},
        ),
        migrations.AlterModelOptions(
            name='clientaccount',
            options={'verbose_name': 'Compte client', 'verbose_name_plural': 'Comptes client'},
        ),
        migrations.AlterModelOptions(
            name='flybooking',
            options={'verbose_name': 'Réservation pour un vol', 'verbose_name_plural': 'Réservations pour un vol'},
        ),
        migrations.AlterModelOptions(
            name='hotelbooking',
            options={'verbose_name': 'Réservation pour un hotel', 'verbose_name_plural': 'Réservations pour un hotel'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Personne', 'verbose_name_plural': 'Personnes'},
        ),
        migrations.AlterField(
            model_name='booking',
            name='client_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.ClientAccount', verbose_name='Compte client lié'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='is_confirmed',
            field=models.BooleanField(verbose_name='Est confirmée'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Courriel'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Nom de famille'),
        ),
        migrations.AlterField(
            model_name='clientaccount',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Numéro de téléphone'),
        ),
        migrations.AlterField(
            model_name='flybooking',
            name='arrival_date',
            field=models.DateTimeField(verbose_name="Date d'arrivée"),
        ),
        migrations.AlterField(
            model_name='flybooking',
            name='arrival_place',
            field=models.CharField(max_length=100, verbose_name="Lieu d'arrivée"),
        ),
        migrations.AlterField(
            model_name='flybooking',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking', verbose_name='Réservation liée'),
        ),
        migrations.AlterField(
            model_name='flybooking',
            name='departure_date',
            field=models.DateTimeField(verbose_name='Date de départ'),
        ),
        migrations.AlterField(
            model_name='flybooking',
            name='departure_place',
            field=models.CharField(max_length=100, verbose_name='Lieu de départ'),
        ),
        migrations.AlterField(
            model_name='flybooking',
            name='is_confirmed',
            field=models.BooleanField(verbose_name='Est confirmée'),
        ),
        migrations.AlterField(
            model_name='flybooking',
            name='number',
            field=models.CharField(max_length=50, verbose_name='Numéro du vol'),
        ),
        migrations.AlterField(
            model_name='flybooking',
            name='price',
            field=models.FloatField(verbose_name='Prix'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='arrival_date',
            field=models.DateTimeField(verbose_name="Date d'arrivée"),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Booking', verbose_name='Réservation liée'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='departure_date',
            field=models.DateTimeField(verbose_name='Date de départ'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='is_confirmed',
            field=models.BooleanField(verbose_name='Est confirmée'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='name',
            field=models.CharField(max_length=100, verbose_name="Nom de l'hotel"),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='place',
            field=models.CharField(max_length=100, verbose_name='Lieu'),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='price',
            field=models.FloatField(verbose_name='Prix'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.DateField(verbose_name='Date de naissance'),
        ),
        migrations.AlterField(
            model_name='person',
            name='client_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.ClientAccount', verbose_name='Compte client lié'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Prénom'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Nom de famille'),
        ),
    ]
