"""Urls related to views for the users app."""
from rest_framework.routers import SimpleRouter

from users.views import ProfileViewSet, UserViewSet


router = SimpleRouter()
router.register('profile', ProfileViewSet, base_name='profile')
router.register('users', UserViewSet, base_name='users')

urlpatterns = router.urls
