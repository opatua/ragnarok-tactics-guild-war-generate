from rest_framework import serializers

from duapola_backend.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'name',
            'is_active'
        )
