from django.db import models
from django.conf import settings


class ReportedIssue(models.Model):
    """Model for reporting building issues/problems."""

    ISSUE_TYPES = [
        ('plumbing', 'Instalație Sanitară'),
        ('electrical', 'Instalație Electrică'),
        ('structural', 'Structural'),
        ('cleaning', 'Curățenie'),
        ('security', 'Securitate'),
        ('other', 'Altele'),
    ]

    STATUS_CHOICES = [
        ('pending', 'În Așteptare'),
        ('in_progress', 'În Progres'),
        ('resolved', 'Rezolvat'),
        ('rejected', 'Respins'),
    ]

    resident_name = models.CharField('Nume Rezident', max_length=100)
    apartment_number = models.CharField('Număr Apartament', max_length=20)
    issue_type = models.CharField('Tip Problemă', max_length=20, choices=ISSUE_TYPES)
    description = models.TextField('Descriere', max_length=1000)
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES, default='pending')
    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reported_issues',
        verbose_name='Raportat de'
    )
    created_at = models.DateTimeField('Creat la', auto_now_add=True)
    updated_at = models.DateTimeField('Actualizat la', auto_now=True)
    resolved_at = models.DateTimeField('Rezolvat la', null=True, blank=True)

    class Meta:
        verbose_name = 'Problemă Raportată'
        verbose_name_plural = 'Probleme Raportate'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.issue_type} - {self.apartment_number} - {self.created_at.strftime('%d.%m.%Y')}"
