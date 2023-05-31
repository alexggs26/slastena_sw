from rest_framework import serializers
from ..models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
    
    def create(self, validated_data):
        created_by = self.context['request'].user.id
        order_data = Orders.objects.create(created_by=created_by, **validated_data)
        return order_data
    
    def update(self, instance, validated_data):
        instance.provider_id = validated_data.get('provider_id', instance.provider_id)
        instance.name = validated_data.get('name', instance.name)
        instance.wholesale_price = validated_data.get('wholesale_price', instance.wholesale_price)
        instance.amount =  validated_data.get('amount', instance.amount)
        instance.purchase_quantity =  validated_data.get('purchase_quantity', instance.purchase_quantity)
        instance.save()
        return instance
    


