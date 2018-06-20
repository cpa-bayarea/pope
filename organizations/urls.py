"""Urls related to views for the organizations app."""
from django.urls import path

from organizations.views import PopeOrganizationFormview


urlpatterns = [
    path('new_organization/', PopeOrganizationFormview.as_view(
        template_name='organization_form.html'), name='new-organization')
]
