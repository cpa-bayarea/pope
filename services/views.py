"""Views for services app."""
from rest_framework import viewsets

from services.models import Area, Subarea, Service
from services.serializers import (ServiceSerializer, AreaSerializer,
                                  SubareaSerializer)


class AreaViewSet(viewsets.ModelViewSet):
    """Views for area endpoints."""
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class SubareaViewSet(viewsets.ModelViewSet):
    """Views for subarea endpoints."""
    queryset = Subarea.objects.all()
    serializer_class = SubareaSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """Views for service endpoints."""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
