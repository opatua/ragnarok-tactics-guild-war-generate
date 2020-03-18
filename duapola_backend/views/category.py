from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from duapola_backend.models import Category
from duapola_backend.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        'id',
        'name',
        'slug',
        'parent_category__name',
        'parent_category__slug'
    )
    ordering_fields = ('slug', 'name', 'created_at', 'updated_at')
    module_slug = 'category'

    def get_queryset(self):
        return Category.objects.order_by('-updated_at')
