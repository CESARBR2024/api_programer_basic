from django.db import models


class ComputersModel(models.Model):
    name = models.CharField(max_length=10)
    marca = models.CharField(max_length=10)
    
