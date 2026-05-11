from django.db import models
from django.conf import settings


class Block(models.Model):
    """Model pentru Clădire/Bloc de locuințe"""
    name = models.CharField(max_length=100, verbose_name='Nume Bloc')
    address = models.CharField(max_length=200, verbose_name='Adresă')
    number_of_floors = models.IntegerField(default=1, verbose_name='Număr Etaje')
    city = models.CharField(max_length=100, default='București', verbose_name='Oraș')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Bloc'
        verbose_name_plural = 'Blocuri'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.address}'


class Apartment(models.Model):
    """Model pentru Apartament"""
    STATUS_CHOICES = [
        ('occupied', 'Ocupat'),
        ('vacant', 'Liber'),
        ('maintenance', 'În Mentenanță'),
    ]

    number = models.CharField(max_length=10, verbose_name='Număr Apartament')
    floor = models.IntegerField(verbose_name='Etaj')
    rooms = models.IntegerField(default=2, verbose_name='Număr Camere')
    area = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Suprafață (mp)')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='apartments', verbose_name='Bloc')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='vacant', verbose_name='Status')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Apartament'
        verbose_name_plural = 'Apartamente'
        ordering = ['block', 'number']

    def __str__(self):
        return f'Apartament {self.number} - {self.block.name}'


class Resident(models.Model):
    """Model pentru Rezident"""
    first_name = models.CharField(max_length=50, verbose_name='Prenume')
    last_name = models.CharField(max_length=50, verbose_name='Nume')
    email = models.EmailField(max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='residents', verbose_name='Apartament')
    active = models.BooleanField(default=True, verbose_name='Activ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Rezident'
        verbose_name_plural = 'Rezidenți'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Manager(models.Model):
    """Model pentru Manager de Bloc"""
    first_name = models.CharField(max_length=50, verbose_name='Prenume')
    last_name = models.CharField(max_length=50, verbose_name='Nume')
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='block_managers', verbose_name='Bloc')
    is_active = models.BooleanField(default=True, verbose_name='Activ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Manager'
        verbose_name_plural = 'Manageri'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.block.name}'


class Administrator(models.Model):
    """Model pentru Administrator de Sistem"""
    first_name = models.CharField(max_length=50, verbose_name='Prenume')
    last_name = models.CharField(max_length=50, verbose_name='Nume')
    email = models.EmailField(max_length=254, unique=True, verbose_name='Email')
    phone = models.CharField(max_length=20, verbose_name='Telefon')
    bloc = models.CharField(max_length=100, blank=True, null=True, verbose_name='Bloc Administrant')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Descriere')
    start_date = models.DateField(null=True, blank=True, verbose_name='Data Începerii')
    end_date = models.DateField(null=True, blank=True, verbose_name='Data Încheierii')

    is_active = models.BooleanField(default=True, verbose_name='Activ')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='created_administrators')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administratori'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'