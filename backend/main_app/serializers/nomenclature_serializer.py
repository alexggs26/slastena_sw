from rest_framework import serializers
from ..models import Nomenclature, Provider_x_Nomenclature


class NomenclatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomenclature
        fields = '__all__'
    
    def create(self, validated_data):
        created_by = self.context['request'].user.id
        nomenclature_data = Nomenclature.objects.create(created_by=created_by, **validated_data)
        return nomenclature_data
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.selling_price = validated_data.get('selling_price', instance.selling_price)
        instance.save()
        return instance

