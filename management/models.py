from django.db import models


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