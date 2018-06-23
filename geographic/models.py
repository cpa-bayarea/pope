"""Models for areas."""
from django.db import models


class AdministrativeArea(models.Model):
    """Model representing administrative areas from a state."""
    name = models.CharField(max_length=50, null=False, blank=False)
    number = models.CharField(max_length=3, null=False, blank=False)
    uf = models.CharField(max_length=2, null=False, blank=False)
