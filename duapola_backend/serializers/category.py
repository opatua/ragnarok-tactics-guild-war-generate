from rest_framework import serializers

from duapola_backend.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['deleted']
