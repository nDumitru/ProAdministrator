from django.db import models

from management.models import Aministrator

class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    trainer = models.ForeignKey(Aministrator, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name