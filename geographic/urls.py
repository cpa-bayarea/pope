"""Urls related to views for the organizations app."""
from rest_framework.routers import SimpleRouter

from geographic.views import AdministrativeAreaViewSet


router = SimpleRouter()
router.register('', AdministrativeAreaViewSet)

urlpatterns = router.urls
