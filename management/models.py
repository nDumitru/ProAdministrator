from django.db import models
from django.conf import settings


class Block(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    number_of_floors = models.IntegerField()
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='managed_blocks')


class Apartment(models.Model):
    number = models.IntegerField()
    floor = models.IntegerField()
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='apartments')


class Resident(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, related_name='residents')


class Manager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='manager_profile')
    phone = models.CharField(max_length=20)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='block_managers')


class Administrator(models.Model):
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    bloc = models.CharField(max_length=15, null=True)
    description = models.TextField(max_length=300, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} - {self.bloc}'
