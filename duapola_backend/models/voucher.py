import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class Voucher(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    code = models.CharField(max_length=255)
    usage_per_voucher = models.IntegerField()
    usage_per_user = models.IntegerField()
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='vouchers_history')

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'vouchers'
