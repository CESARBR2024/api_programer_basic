from rest_framework import serializers
from .models import ComputersModel

class ComputersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputersModel
        fields='__all__'
