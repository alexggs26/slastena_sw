from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser 
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from ..serializers.nomenclature_serializer import NomenclatureSerializer
from ..models import Nomenclature

class NomenclatureView(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = NomenclatureSerializer

    @csrf_exempt
    def get(self, request, pk=None):
        objects = Nomenclature.objects.get(pk=pk) if pk else Nomenclature.objects.all()
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
            nomenclature = Nomenclature.objects.get(pk=pk)
        except Nomenclature.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'nomenclature does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            nomenclature_data = JSONParser().parse(request)
            serializer = self.serializer_class(nomenclature, data=nomenclature_data, context={'request': request})
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
            nomenclature = Nomenclature.objects.get(pk=pk)
        except Nomenclature.DoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'message': 'nomenclature does not exist', 
                'status': status_code
            }
            return Response(response, status=status_code)
        else:
            nomenclature.delete()
            status_code = status.HTTP_204_NO_CONTENT
            response = {
                'message': 'nomenclature was deleted successfully!',
                'status_code': status_code
            }
            return Response(response, status=status_code)