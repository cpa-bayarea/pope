"""Urls related to views for the organizations app."""
from rest_framework.routers import SimpleRouter

from organizations.views import (OrganizationViewset,
                                 ScheduleViewset)

router = SimpleRouter()
router.register('', OrganizationViewset)
router.register('schedules', ScheduleViewset)

urlpatterns = router.urls
