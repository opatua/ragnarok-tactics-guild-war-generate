from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from duapola_backend.models import City
from duapola_backend.serializers import CitySerializer


class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        'id',
        'name',
        'slug',
    )
    ordering_fields = ('slug', 'name', 'created_at', 'updated_at')
    module_slug = 'city'

    def get_queryset(self):
        return City.objects.order_by('-updated_at')
