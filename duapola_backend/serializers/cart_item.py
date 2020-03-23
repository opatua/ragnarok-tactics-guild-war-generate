from rest_framework import serializers

from duapola_backend.models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    cart_id = serializers.PrimaryKeyRelatedField(
        queryset=Cart.objects.all(),
        source='cart',
        write_only=True,
    )

    class Meta:
        model = CartItem
        exclude = ['deleted']
