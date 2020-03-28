import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class PromotionVoucher(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    promotion = models.ForeignKey(
        'Promotion',
        on_delete=models.SET_NULL,
        null=True
    )
    voucher = models.ForeignKey(
        'Voucher',
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='promotions_history')

    class Meta:
        db_table = 'promotions'
