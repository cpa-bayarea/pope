"""Models for services."""
from django.db import models

from organizations.models import Organization
from geographic.models import AdministrativeArea


class Area(models.Model):
    """Model representing an knowledge area for services."""
    name = models.CharField(max_length=30, null=False, blank=False)


class Subarea(models.Model):
    """Model representing a specific subarea of Area."""
    name = models.CharField(max_length=30, null=False, blank=False)
    area = models.ForeignKey(
        Area, null=False, related_name="subareas", on_delete=models.CASCADE)


class Service(models.Model):
    """Model representing a provided service."""
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    provider = models.ForeignKey(
        Organization, null=False, on_delete=models.CASCADE)
    administrative_area = models.ForeignKey(
        AdministrativeArea, null=False, on_delete=models.CASCADE)
    subarea = models.ForeignKey(Subarea, null=False, on_delete=models.CASCADE)
    is_free = models.BooleanField(null=False, default=True)
