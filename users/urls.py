"""Urls related to views for the users app."""
from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import PopeUserFormView, DashboardView


urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path('new_user/', PopeUserFormView.as_view(), name='new-user')
]
