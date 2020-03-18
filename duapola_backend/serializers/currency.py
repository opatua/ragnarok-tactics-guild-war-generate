from rest_framework import serializers

from duapola_backend.models import Currency


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        exclude = ['deleted']
