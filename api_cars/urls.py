from django.urls import path, include
from rest_framework import routers
from api_cars import views

router=routers.DefaultRouter()
router.register(r'cars', views.CarsViewSets)

urlpatterns = [
    path('', include(router.urls))
]