from django.db import models

class CarsModel(models.Model):
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=50)
    age_model = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)
