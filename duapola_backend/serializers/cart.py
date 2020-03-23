from rest_framework import serializers

from duapola_backend.models import User, Cart, CartItem, Product
from duapola_backend.serializers.cart_item import CartItemSerializer
from duapola_backend.serializers.user import UserSerializer


class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        read_only=True
    )

    cart_items = serializers.SerializerMethodField()

    def get_cart_items(self, cart):
        cart_items = CartItem.objects.filter(cart=cart)
        print(CartItemSerializer(instance=cart_items, many=True).data)

        return CartItemSerializer(instance=cart_items, many=True).data

    def create(self, validated_data):
        if self.context['request'].user and self.context['request'].user.id:
            validated_data = self._update_params(
                validated_data,
                self.context['request'].user
            )
            cart = Cart.objects.filter(user=self.context['request'].user)
            cart.delete()

        cart = super().create(validated_data)
        self._create_cart_items(
            self.context['request'].data.get('cart_items'),
            cart
        )

        return cart

    def update(self, instance, validated_data):
        if self.context['request'].user and self.context['request'].user.id:
            validated_data = self._update_params(
                validated_data,
                self.context['request'].user
            )

        cart = super().update(instance, validated_data)
        self._create_cart_items(
            self.context['request'].data.get('cart_items'),
            cart
        )

        return cart

    def _update_params(self, data, user):
        data['user_id'] = str(user.id)

        return data

    def _create_cart_items(self, cart_items_data, cart):
        cart_items = CartItem.objects.filter(cart=cart)
        if cart_items:
            cart_items.delete()

        for cart_item_data in cart_items_data:
            cart_item_data['cart_id'] = cart.id
            product = Product.objects.filter(
                id=cart_item_data.get('product_id')
            ).first()
            if not product:
                continue

            price = cart_item_data.get('quantity') * product.price
            cart_item_data['price'] = price

            cart_item_serializer = CartItemSerializer(data=cart_item_data)
            cart_item_serializer.is_valid(raise_exception=True)
            cart_item_serializer.save()

    class Meta:
        model = Cart
        exclude = ['deleted']
