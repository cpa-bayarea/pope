from django.views.generic.edit import FormView
from rest_framework import viewsets

from organizations.forms import PopeOrganizationForm
from organizations.models import Organization, Schedule
from organizations.serializers import (OrganizationSerializer,
                                       ScheduleSerializer)


class PopeOrganizationFormview(FormView):
    template_name = 'organization_form.html'
    form_class = PopeOrganizationForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class OrganizationViewset(viewsets.ModelViewSet):
    """Views for organization endpoints."""
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ScheduleViewset(viewsets.ModelViewSet):
    """Views for schedule endpoints."""
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
