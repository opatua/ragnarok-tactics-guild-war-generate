import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords

from duapola_backend.enums import CartStatus


class Cart(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        'User',
        on_delete=models.SET_NULL,
        null=True
    )
    status = models.CharField(
        max_length=255,
        default=CartStatus.PENDING.value
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='carts_history')

    class Meta:
        db_table = 'carts'
