from rest_framework import serializers

from duapola_backend.models import Color


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        exclude = ['deleted']
