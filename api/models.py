from django.db import models

class Programer(models.Model):
    fullname = models.CharField(max_length=255)
    nickname = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)


