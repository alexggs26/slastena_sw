from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from ..serializers.user_serializer import UserRegistrationSerializer, UserLoginSerializer
from ..models import User


class UserRegistrationView(APIView):

    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer
    
    @csrf_exempt
    def get(self, request):
        objects = User.objects.all()
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
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'user': serializer.data['email']
            }
        return Response(response, status=status_code)


class UserLoginView(APIView):

    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    @csrf_exempt
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        status_code = status.HTTP_200_OK
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User logged in successfully',
            'user': serializer.data['email'],
            'token': serializer.data['token'],
            }
        return Response(response, status=status_code)