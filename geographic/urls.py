"""Urls related to views for the organizations app."""
from django.urls import path
from rest_framework.routers import SimpleRouter

from geographic.views import AdministrativeAreaViewSet
                                
                                

router  = SimpleRouter()
router.register('', AdministrativeAreaViewSet)

urlpatterns = router.urls
