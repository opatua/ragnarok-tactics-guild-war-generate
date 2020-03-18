from rest_framework import serializers

from duapola_backend.models import Country


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        exclude = ['deleted']
