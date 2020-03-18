from rest_framework import serializers

from duapola_backend.models import ProductFamily


class ProductFamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductFamily
        exclude = ['deleted']
