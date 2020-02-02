import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords
from slugify import slugify


class Address(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    address = models.TextField()
    postal_code = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='addresses_history')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'addresses'
