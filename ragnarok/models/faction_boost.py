import uuid

from django.contrib.postgres.fields import JSONField
from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class FactionBoost(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
