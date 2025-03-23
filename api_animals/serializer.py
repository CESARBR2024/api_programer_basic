from rest_framework import serializers
from .models import AnimalsModel

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalsModel
        fields = '__all__'