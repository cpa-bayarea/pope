"""Urls related to views for the organizations app."""
from django.urls import path
from rest_framework.routers import SimpleRouter

from organizations.views import (PopeOrganizationFormview,
                                 OrganizationViewset,
                                 ScheduleViewset)

router  = SimpleRouter()
router.register(r'^', OrganizationViewset)
router.register(r'^schedules', ScheduleViewset)

urlpatterns = router.urls
