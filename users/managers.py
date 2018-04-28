from django.contrib.auth.models import BaseUserManager


class PopeUserManager(BaseUserManager):
    """User manager pope, customizing username field."""

    user_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """Create and save a user with its email and password."""
        if not email:
            raise ValueError('O usuário deve conter um email.')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        """Create a non-super nor staff user, set as inactive."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('user_type', 'A')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff deve ser True para um super usuário')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'is_superuser deve ser True para um super usuário'
            )

        return self._create_user(username, email, password, **extra_fields)
