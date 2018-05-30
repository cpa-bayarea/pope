"""Django user customization for PoPe."""
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import PopeUserManager


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
    is_active = models.BooleanField(max_length=3, null=False, default=False)

    REQUIRED_FIELDS = ['email']
    objects = PopeUserManager()
