from django.contrib.auth import authenticate
from django.http import JsonResponse
from http import HTTPStatus
from rest_framework_jwt.settings import api_settings
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from duapola_backend.models import User
from duapola_backend.serializers import UserSerializer


class SignInView(CreateAPIView):
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if not(email and password):
            return JsonResponse(
                {'errors': 'Request not valid!'},
                status=HTTPStatus.BAD_REQUEST
            )

        user = authenticate(request, email=email, password=password)

        if not user:
            return JsonResponse(
                {'errors': 'Email or password is invalid!'},
                status=HTTPStatus.BAD_REQUEST
            )

        payload = {
            'token': self._generate_token(user),
            'user': UserSerializer(instance=user).data
        }

        return JsonResponse(
            payload,
            status=HTTPStatus.OK
        )

    def _generate_token(self, user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)

        return jwt_encode_handler(payload)
