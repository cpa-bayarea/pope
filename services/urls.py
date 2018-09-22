"""Urls related to views for the services app."""
from django.urls import path
from rest_framework.routers import SimpleRouter

from services.views import (ServiceViewSet, AreaViewSet,
                                 SubareaViewSet)


router  = SimpleRouter()
router.register('', ServiceViewSet)
router.register('areas', AreaViewSet)
router.register('subareas', SubareaViewSet)

urlpatterns = router.urls