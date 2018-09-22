"""Serializers for geographic app."""
from rest_framework import serializers
from geographic.models import AdministrativeArea


class AdministrativeAreaSerializer(serializers.ModelSerializer):
    """Serializer for Administrative Areas."""
    class Meta:
        """Default Meta class."""
        model = AdministrativeArea
        fields = '__all__'