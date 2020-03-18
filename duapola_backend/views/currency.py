from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from duapola_backend.models import Currency
from duapola_backend.serializers import CurrencySerializer


class CurrencyViewSet(ModelViewSet):
    serializer_class = CurrencySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        'id',
        'name',
    )
    ordering_fields = ('id', 'name', 'created_at', 'updated_at')
    module_slug = 'currency'

    def get_queryset(self):
        return Currency.objects.order_by('-updated_at')
