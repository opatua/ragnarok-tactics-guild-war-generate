from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from duapola_backend.models import Product
from duapola_backend.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        'id',
        'name',
        'slug',
        'product_family__name',
        'product_family__slug',
    )
    ordering_fields = ('created_at', 'updated_at')
    module_slug = 'product'

    def get_queryset(self):
        return Product.objects.order_by('-updated_at')
