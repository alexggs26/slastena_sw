from rest_framework import serializers
from ..models import Provider, Provider_Requisits, Provider_x_Contact, Contact


class RequisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider_Requisits
        fields = '__all__'
        
    def create(self, **validated_data):
        created_by = self.context['request'].user.id
        requisit_data = Provider_Requisits.objects.create(created_by=created_by, **validated_data)
        return requisit_data
    
    def update(self, instance, **validated_data):
        instance.inn = validated_data.get('inn', instance.inn)
        instance.ogrn = validated_data.get('ogrn', instance.ogrn)
        instance.address = validated_data.get('address', instance.address)
        instance.org_type = validated_data.get('org_type', instance.org_type)
        instance.bank_name = validated_data.get('bank_name', instance.bank_name)
        instance.bank_account = validated_data.get('bank_account', instance.bank_account)
        instance.bank_cors_account = validated_data.get('bank_cors_account', instance.bank_cors_account)
        instance.save()
        return instance
        
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
    
    def create(self, **validated_data):
        created_by = self.context['request'].user.id
        contact_data = Contact.objects.create(created_by=created_by, **validated_data)
        return contact_data
    
    def update(self, instance, **validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.birthday_date = validated_data.get('birthday_date', instance.birthday_date)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance 
    
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
        created_by = self.context['request'].user.id
        provider_data = Provider.objects.create(created_by=created_by, **validated_data)
        return provider_data

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.date_create = validated_data.get('title', instance.date_create)
        instance.save()
        return instance 

