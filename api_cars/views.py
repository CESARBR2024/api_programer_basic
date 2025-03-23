from django.shortcuts import render
from .serializer import CarsSerializer
from .models import CarsModel
from rest_framework import viewsets

class CarsViewSets(viewsets.ModelViewSet):
    queryset=CarsModel.objects.all()
    serializer_class=CarsSerializer
    
