from django.shortcuts import render
from .serializer import ComputersSerializer
from .models import ComputersModel
from rest_framework import viewsets

class ComputerViewSet(viewsets.ModelViewSet):
    queryset = ComputersModel.objects.all()
    serializer_class = ComputersSerializer

# Create your views here.
