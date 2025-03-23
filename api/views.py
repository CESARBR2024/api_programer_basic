from django.shortcuts import render
from .serializer import ProgramerSerializer
from .models import Programer
from rest_framework import viewsets

class ProgramerViewSet(viewsets.ModelViewSet):
    queryset=Programer.objects.all()
    serializer_class = ProgramerSerializer




