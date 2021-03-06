"""pope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.urls import path
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('', include('users.urls')),
    path('organizations/', include('organizations.urls')),
    path('geo/', include('geographic.urls')),
    path('services/', include('services.urls')),
    url(r'^api-auth/', views.obtain_auth_token),
    url(r'^docs/', include_docs_urls(title='API PoPe')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
