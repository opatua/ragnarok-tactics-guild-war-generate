from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from duapola_backend.models import Country
from duapola_backend.serializers import CountrySerializer


class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        'id',
        'name',
    )
    ordering_fields = ('id', 'name', 'created_at', 'updated_at')
    module_slug = 'country'

    def get_queryset(self):
        return Country.objects.order_by('-updated_at')
