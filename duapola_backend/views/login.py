from django.contrib.auth import authenticate
from http import HTTPStatus
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from duapola_backend.models import User
from duapola_backend.serializers import UserSerializer
from duapola_backend.services import Token


class LoginView(CreateAPIView):
    permission_classes = (AllowAny,)

    def __init__(self):
        self._token = Token()

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        payload = None

        if not(email and password):
            return Response({'detail': 'Request not valid!'}, status=HTTPStatus.BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if not user:
            return Response({'detail': 'Email or password is not exists!'}, status=HTTPStatus.BAD_REQUEST)

        payload = {
            'token': self._token.generate(user),
            'user': UserSerializer(instance=user).data
        }

        return Response(payload)
