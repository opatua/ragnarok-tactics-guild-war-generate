from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from duapola_backend.models import Cart
from duapola_backend.serializers import CartSerializer


class CartViewSet(ModelViewSet):
    serializer_class = CartSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = (
        'id',
        'user__name',
        'user__email'
    )
    ordering_fields = ('created_at', 'updated_at')
    module_slug = 'cart'

    def get_queryset(self):
        if self.request.user and self.request.user.id:
            cart = Cart.objects.filter(user=self.request.user)
            if cart:
                return cart

        return Cart.objects.none()
