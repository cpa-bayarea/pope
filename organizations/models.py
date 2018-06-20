"""Django organizations customizations for pope """
from django.db import models


class Organization(models.Model):
    # Atributes
    org_name = models.CharField(max_length=35, null=False,
                                blank=False, default=False)
    cnpj = models.CharField(max_length=15, null=False,
                            blank=False, default=False)
    social_reason = models.CharField(max_length=25, null=False,
                                     blank=False, default=False)
    email = models.EmailField(null=False, blank=False, default=False)
    telephone = models.CharField(max_length=11, null=False,
                                 blank=False, default=False)

    REQUIRED_FIELDS = ['name', 'email', 'cnpj']
