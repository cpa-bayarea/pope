"""Views for geographic app."""
from rest_framework.viewsets import ModelViewSet

from geographic.models import AdministrativeArea
from geographic.serializers import AdministrativeAreaSerializer


class AdministrativeAreaViewSet(ModelViewSet):
    """Views for administrative areas endpoints."""
    queryset = AdministrativeArea.objects.all()
    serializer_class = AdministrativeAreaSerializer