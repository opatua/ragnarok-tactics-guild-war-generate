from rest_framework.generics import CreateAPIView
from http import HTTPStatus
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from random import randint

from duapola_backend.models import User
from duapola_backend.serializers import RegisterSerializer, UserSerializer
from duapola_backend.services import Token


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)

    def __init__(self):
        self._token = Token()

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = User.objects.filter(
                email=request.data.get('email')
            )

            if user:
                return Response({'detail': 'User within given phone number is exist, Please Login.'}, status=HTTPStatus.BAD_REQUEST)

            data = {
                'email': serializer.validated_data['email'],
                'password': serializer.validated_data['password'],
                'name': serializer.validated_data['name']
            }

            user = User.objects.create_user(**data)

            payload = {
                'data': {
                    'token': self._token.generate(user),
                    'user': UserSerializer(instance=user).data
                }
            }

            return Response(payload, status=HTTPStatus.CREATED)
