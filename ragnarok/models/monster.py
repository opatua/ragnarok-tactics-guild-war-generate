import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords

from ragnarok.enums import FactionEnum, MonsterTypeEnum


class Monster(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    faction = models.CharField(
        max_length=255,
        choices=FactionEnum.choices(),
    )
    type = models.CharField(
        max_length=255,
        choices=MonsterTypeEnum.choices(),
        null=True,
    )
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
