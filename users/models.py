"""Django user customization for PoPe."""
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import PopeUserManager
from organizations.models import Organization


class User(AbstractUser):
    """Customize user model.

    We need to implement types and is_active flag.
    """
    USER_TYPE_CHOICES = (
        ('A', 'Admin'),
        ('AG', 'Agente'),
        ('P', 'Prestador'),
    )

    user_type = models.CharField(max_length=3, null=False,
                                 blank=False, default='P')
    is_active = models.BooleanField(null=False, default=True)
    is_authorized = models.BooleanField(null=False, default=False)
    organization = models.ForeignKey(Organization,
                                     null=True, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['email']
    objects = PopeUserManager()
