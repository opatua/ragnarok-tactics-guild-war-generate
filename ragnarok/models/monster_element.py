import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords

from ragnarok.enums import ElementEnum


class MonsterElement(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    monster = models.ForeignKey(
        'Monster',
        on_delete=models.CASCADE,
        related_name='elements',
    )
    element = models.CharField(
        max_length=255,
        choices=ElementEnum.choices(),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.monster.name} - {self.element}'
