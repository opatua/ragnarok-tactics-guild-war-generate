from rest_framework import serializers

from duapola_backend.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        exclude = ['deleted']
