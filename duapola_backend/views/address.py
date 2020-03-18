from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from duapola_backend.models import Address
from duapola_backend.serializers import AddressSerializer


class AddressViewSet(ModelViewSet):
    serializer_class = AddressSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ('id', 'city__name', 'user__email', 'postal_code')
    ordering_fields = ('user__email', 'created_at', 'updated_at')
    module_slug = 'address'

    def get_queryset(self):
        return Address.objects.filter(user=self.request.user).order_by('-updated_at')
