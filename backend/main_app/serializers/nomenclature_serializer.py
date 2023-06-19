from rest_framework import serializers
from ..models import Nomenclature, Provider_x_Nomenclature


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        fields = '__all__'
    
    def create(self, validated_data):
        nomenclature_data = Nomenclature.objects.create( **validated_data)
        return nomenclature_data
