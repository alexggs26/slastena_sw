from rest_framework import serializers
from ..models import Provider, Provider_Requisits, Provider_x_Contact, Contact
from .user_serializer import UserRegistrationSerializer

class RequisitSerializer(serializers.ModelSerializer):
    created_by = UserRegistrationSerializer()
    class Meta:
        model = Provider_Requisits
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    created_by = UserRegistrationSerializer()
    class Meta:
        model = Contact
        fields = '__all__'
 
class ProviderSerializer(serializers.ModelSerializer):
    created_by = UserRegistrationSerializer()
    class Meta:
        model = Provider
        fields = '__all__' 



