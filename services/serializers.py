"""Serializers for services app."""
from rest_framework import serializers

from services.models import (Area, Subarea, Service)


class AreaSerializer(serializers.ModelSerializer):
    """Serializer for area model."""
    class Meta:
        """Default meta class."""
        model = Area
        fields = '__all__'


class SubareaSerializer(serializers.ModelSerializer):
    """Serializer for subarea model."""
    class Meta:
        """Default meta class."""
        model = Subarea
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    """Serializer for service model."""
    class Meta:
        """Default meta class."""
        model = Service
        fields = '__all__'
