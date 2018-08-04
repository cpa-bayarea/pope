"""Classes for forms related to organizations."""

from django.forms import ModelForm

from services.models import Service


class ServiceForm(ModelForm):
    class Meta:
        """Meta default."""
        model = Service
        exclude = ('provider')
