from django.db import models

class AnimalsModel(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    extincion = models.BooleanField(default=True)
