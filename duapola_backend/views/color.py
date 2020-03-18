from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from duapola_backend.models import Color
from duapola_backend.serializers import ColorSerializer


class ColorViewSet(ModelViewSet):
    serializer_class = ColorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        'id',
        'name',
        'slug',
    )
    ordering_fields = ('slug', 'name', 'created_at', 'updated_at')
    module_slug = 'color'

    def get_queryset(self):
        return Color.objects.order_by('-updated_at')
