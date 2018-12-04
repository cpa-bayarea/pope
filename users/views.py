from rest_framework import viewsets

from users.models import User
from users.serializers import UserSerializer, ProfileSerializer
from users.permissions import IsStaffOrSelf, IsAdminOrRegister


class UserViewSet(viewsets.ModelViewSet):
    """Endpoints for admin users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrRegister]


class ProfileViewSet(viewsets.ModelViewSet):
    """Enpoints for profile."""
    serializer_class = ProfileSerializer
    model = User
    permission_classes = [IsStaffOrSelf]
