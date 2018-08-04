"""Urls related to views for the services app."""
from django.urls import path

from organizations.views import PopeOrganizationFormview


urlpatterns = [
    path('<int:user_id>/new_organization/', ServiceFormView.as_view(),
         name='new-organization')
]
