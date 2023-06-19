from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from ..serializers.provider_serializer import *
from ..models import Provider, Provider_Requisits, Provider_x_Contact, Contact

created_by = get_user_model()        
class ProviderView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProviderSerializer
    
    @csrf_exempt
    def get(self, request, pk=None):
        objects = Provider.objects.filter(pk=pk) if pk else  Provider.objects.all()
        serializer = self.serializer_class(objects, many=True)
        status_code = status.HTTP_200_OK
        response = {
            'success': 'True',
            'status_code': status_code,
            'items': serializer.data
            }
        return Response(response, status=status_code)
    
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status_code': status_code,
            'item': serializer.data
            }
        return Response(response, status=status_code)
    
    @csrf_exempt
    def put(self, request, pk):
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'provider does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            provider_data = JSONParser().parse(request)
            serializer = self.serializer_class(provider, data=provider_data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'True',
                'status_code': status_code,
                'item': serializer.data
            }
            return Response(response, status=status_code)
        
        
    @csrf_exempt
    def delete(self, request, pk):
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'provider does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            provider.delete()
            status_code = status.HTTP_204_NO_CONTENT
            response = {
                'message': 'provider was deleted successfully!',
                'status_code': status_code
            }
            return Response(response, status=status_code)
        

class RequisitsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RequisitSerializer
    
    @csrf_exempt
    def get(self, request, pk):
        objects = Provider_Requisits.objects.filter(provider_id=pk)
        serializer = self.serializer_class(objects, many=True)
        status_code = status.HTTP_200_OK
        response = {
            'success': 'True',
            'status_code': status_code,
            'items': serializer.data
            }
        return Response(response, status=status_code)
    
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status_code': status_code,
            'item': serializer.data
            }
        return Response(response, status=status_code)
    
    @csrf_exempt
    def put(self, request, pk):
        try:
            requisit = Provider_Requisits.objects.get(provider_id=pk)
        except Provider_Requisits.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'requisit does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            requisit_data = JSONParser().parse(request)
            serializer = self.serializer_class(requisit, data=requisit_data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'True',
                'status_code': status_code,
                'item': serializer.data
            }
            return Response(response, status=status_code)
        
    @csrf_exempt
    def delete(self, request, pk):
        try:
            requisit = Provider_Requisits.objects.get(provider_id=pk)
        except Provider_Requisits.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'requisit does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            requisit.delete()
            status_code = status.HTTP_204_NO_CONTENT
            response = {
                'message': 'requisit was deleted successfully!',
                'status_code': status_code
            }
            return Response(response, status=status_code)
    
    
class ContactsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer
    
    @csrf_exempt
    def get(self, request, pk):
        contact_id = Provider_x_Contact.objects.filter(provider_id=pk).values('contact_id')
        objects = Contact.objects.filter(id__in=contact_id)
        serializer = self.serializer_class(objects, many=True)
        status_code = status.HTTP_200_OK
        response = {
            'success': 'True',
            'status_code': status_code,
            'items': serializer.data
            }
        return Response(response, status=status_code)
    
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status_code': status_code,
            'item': serializer.data
            }
        return Response(response, status=status_code)
    
    @csrf_exempt
    def put(self, request, pk):
        try:
            contact = Contact.objects.get(id=pk)
        except Contact.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'Contact does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            contact_data = JSONParser().parse(request)
            serializer = self.serializer_class(contact, data=contact_data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            status_code = status.HTTP_200_OK
            response = {
                'success': 'True',
                'status_code': status_code,
                'item': serializer.data
            }
            return Response(response, status=status_code)
             
    @csrf_exempt
    def delete(self, request, pk):
        try:
            contact_id =  Provider_x_Contact.objects.filter(provider_id=pk).values('contact_id')
            contact = Contact.objects.filter(id__in=contact_id)
        except Contact.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'Contact does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            contact.delete()
            status_code = status.HTTP_204_NO_CONTENT
            response = {
                'message': 'contact was deleted successfully!',
                'status_code': status_code
            }
            return Response(response, status=status_code)
 
        
class ContactLinkView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Provider_x_ContactSerializer
    
    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status_code': status_code,
            'item': serializer.data
            }
        return Response(response, status=status_code)
    
    @csrf_exempt
    def delete(self, request):
        try:
            pk = request.data['provider_id']
            contact_id =  Provider_x_Contact.objects.filter(provider_id=pk).values('contact_id')
            contact = Contact.objects.filter(id__in=contact_id)
        except Contact.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'Contact does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            contact.delete()
            status_code = status.HTTP_204_NO_CONTENT
            response = {
                'message': 'contact was deleted successfully!',
                'status_code': status_code
            }
            return Response(response, status=status_code)