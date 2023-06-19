from rest_framework import serializers
from ..models import Orders


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
    
    def create(self, validated_data):
        order_data = Orders.objects.create(**validated_data)
        return order_data
