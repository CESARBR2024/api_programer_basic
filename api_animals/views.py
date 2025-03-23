from django.shortcuts import render
from .serializer import AnimalSerializer
from .models import AnimalsModel
from rest_framework import viewsets

class AnimalViewSet(viewsets.ModelViewSet):
    queryset=AnimalsModel.objects.all()
    serializer_class=AnimalSerializer

