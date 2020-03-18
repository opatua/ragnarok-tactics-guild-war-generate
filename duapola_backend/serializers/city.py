from rest_framework import serializers

from duapola_backend.models import City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        exclude = ['deleted']
