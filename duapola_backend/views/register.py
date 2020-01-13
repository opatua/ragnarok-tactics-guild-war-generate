from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from http import HTTPStatus
from rest_framework.permissions import AllowAny
from random import randint

from duapola_backend.models import User
from duapola_backend.serializers import RegisterSerializer, UserSerializer


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = User.objects.filter(
                email=request.data.get('email')
            )

            if user:
                return JsonResponse(
                    {'errors': 'User within given phone number is exist, Please Login.'},
                    status=HTTPStatus.BAD_REQUEST
                )

            data = {
                'email': serializer.validated_data['email'],
                'password': serializer.validated_data['password'],
                'name': serializer.validated_data['name']
            }

            user = User.objects.create_user(**data)
            user_serializer = UserSerializer(user)

            return JsonResponse(
                user_serializer.data,
                status=HTTPStatus.CREATED
            )
