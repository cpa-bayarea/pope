from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        exclude = ('date_joined', 'is_superuser',
                   'groups', 'user_permissions', 'last_login')
        read_only_fields = ['is_superuser']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        exclude = ('date_joined', 'is_superuser',
                   'groups', 'user_permissions', 'last_login')
        read_only_fields = ['is_superuser', 'is_staff',
                            'user_type', 'is_active']
