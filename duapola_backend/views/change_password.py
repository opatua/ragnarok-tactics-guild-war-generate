from django.contrib.auth import get_user_model
from http import HTTPStatus
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from duapola_backend.serializers import ChangePasswordSerializer, UserSerializer


class ChangePasswordView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        user = self.request.user
        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')
        old_password = request.data.get('old_password')

        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if not user.check_password(old_password):
                return Response(
                    {'detail': 'Email or password not valid'},
                    status=HTTPStatus.BAD_REQUEST
                )

            if new_password != confirm_password:
                return Response(
                    {'errors': 'Password and Confirmation Password not same'},
                    status=HTTPStatus.BAD_REQUEST
                )

            user.set_password(new_password)
            user.save()

            user_serializer = UserSerializer(instance=user)

            return Response(
                {'user': user_serializer.data},
                status=HTTPStatus.OK
            )
