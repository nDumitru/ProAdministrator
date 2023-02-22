from django.db import models

from management.models import Administrator


class Resident(models.Model):

    gender_options = (('male', 'Male'), ('female', 'Female'))

    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    age = models.IntegerField()
    chirias = models.BooleanField(default=False)
    email = models.EmailField(max_length=50, null=True)
    description = models.TextField(max_length=300, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    administrator = models.ForeignKey(Administrator, on_delete=models.CASCADE, null=True)

    gender = models.CharField(max_length=6, choices=gender_options, null=True)

    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
