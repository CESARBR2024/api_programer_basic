from django.urls import path, include
from rest_framework import routers
from api import views

#Elemento que permite manejar multiples rutas
router=routers.DefaultRouter()
router.register(r'programers', views.ProgramerViewSet) #Base de este endpoint

urlpatterns = [
    path('', include(router.urls))
]



