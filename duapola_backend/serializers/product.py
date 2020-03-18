from rest_framework import serializers

from duapola_backend.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ['deleted']
