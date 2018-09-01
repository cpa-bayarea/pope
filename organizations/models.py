"""Django organizations customizations for pope """
from django.db import models


class Organization(models.Model):
    """Organization model."""
    org_name = models.CharField(max_length=35, null=False,
                                blank=False, default=False)
    email = models.EmailField(null=False, blank=False,
                              unique=True, default=False)
    telephone = models.CharField(max_length=11, null=False,
                                 blank=False, default=False)
    cep = models.CharField(max_length=8, null=True, blank=True)
    neighbourhood = models.CharField(max_length=255, null=True, blank=True)
    addr = models.CharField(max_length=255, null=False, blank=False)
    additional_addr = models.CharField(max_length=50,
                                       null=False, blank=False)


class Schedule(models.Model):
    """Schedule for each organization work day."""
    WEEK_DAY_CHOICES = (
        (1, 'Domingo'),
        (2, 'Segunda-feira'),
        (3, 'Terça-feira'),
        (4, 'Quarta-feira'),
        (5, 'Quinta-feira'),
        (6, 'Sexta-feira'),
        (7, 'Sábado'),
    )
    time_from = models.TimeField(null=False, blank=False)
    time_to = models.TimeField(null=False, blank=False)
    week_day = models.IntegerField(null=False, choices=WEEK_DAY_CHOICES)
    organization = models.ForeignKey(Organization,
                                     on_delete=models.CASCADE,
                                     related_name='schedules')
