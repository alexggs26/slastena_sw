from rest_framework import serializers
from ..models import Provider, Provider_Requisits, Provider_x_Contact, Contact


class RequisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider_Requisits
        fields = '__all__'
        
    def create(self, validated_data):
        requisit_data = Provider_Requisits.objects.create(**validated_data)
        return requisit_data
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
    
    def create(self, validated_data):
        contact_data = Contact.objects.create(**validated_data)
        return contact_data
    
    
class Provider_x_ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider_x_Contact
        fields = '__all__'
        
    def create(self, validated_data):
        data = Provider_x_Contact.objects.create(**validated_data)
        return data
    
 
class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__' 

    def create(self, validated_data):
        provider_data = Provider.objects.create(**validated_data)
        return provider_data



