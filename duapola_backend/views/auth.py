from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_jwt.settings import api_settings

from duapola_backend.utils.api_response import response
from duapola_backend.serializers.auth import LoginSerializer, RegisterSerializer
from duapola_backend.serializers.user import UserSerializer
from duapola_backend.models.user import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(APIView):

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)

                user_serializer = UserSerializer(user)

                payload = {
                    'token': token,
                    'user': user_serializer.data
                }
                return response(status.HTTP_200_OK, 'success', payload)
            else:
                return response(status.HTTP_400_BAD_REQUEST, 'Invalid Login! Email or Password Missmatch.', '')


class RegisterView(APIView):

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            data = {
                'email': serializer.validated_data['email'],
                'password': serializer.validated_data['password'],
                'name': serializer.validated_data['name']
            }

            is_exist = User.objects.get(
                email=serializer.validated_data['email'])

            if is_exist:
                return response(status.HTTP_400_BAD_REQUEST, 'User within given email is exist, Please Login.', data=None)

            user = User.objects.create_user(**data)
            user_serializer = UserSerializer(user)

            return response(status.HTTP_200_OK, 'success', user_serializer.data)
