"""Django organizations customizations for pope """
from django.db import models

from organizations.validators import validate_CNPJ


class Organization(models.Model):
    # Atributes
    org_name = models.CharField(max_length=35, null=False,
                                blank=False, default=False)
    cnpj = models.CharField(max_length=15, null=False, unique=True,
                            blank=False, default=False,
                            validators=[validate_CNPJ])
    social_reason = models.CharField(max_length=25, null=False,
                                     blank=False, default=False)
    email = models.EmailField(null=False, blank=False,
                              unique=True, default=False)
    telephone = models.CharField(max_length=11, null=False,
                                 blank=False, default=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    additional_addr = models.CharField(max_length=50,
                                       null=False, blank=False)
