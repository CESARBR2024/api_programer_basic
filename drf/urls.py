"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='API for Programer',
        default_version='v1',
        description='Api for add/get/delete and put programers',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='cesar.barcenas@imberacooling.com'),
        licese=openapi.License(name='BSD License'),
    ),
    public=True,
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_programer/app/', include('api.urls') ),
    path('api_cars/app/', include('api_cars.urls') ),
    path('api_animals/app/', include('api_animals.urls') ),
    path('swagger/', schema_view.with_ui('swagger',
     cache_timeout=0), name='schema-swagger-ui'),
]
