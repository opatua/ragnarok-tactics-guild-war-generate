import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class CartItem(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.SET_NULL,
        null=True
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=20,
        decimal_places=4,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='cart_itemss_history')

    class Meta:
        db_table = 'cart_items'
