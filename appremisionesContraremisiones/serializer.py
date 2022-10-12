from .models import Remision_Contraremision, Acompanante
from rest_framework import serializers

class RemisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Remision_Contraremision
        fields = '__all__'


class AcompananteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acompanante
        fields = '__all__'