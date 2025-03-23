from django.urls import path, include
from rest_framework import routers
from api_computers import views

router = routers.DefaultRouter()
router.register(r'computer', views.ComputerViewSet)

urlpatterns = [
    path('', include(router.urls))
]