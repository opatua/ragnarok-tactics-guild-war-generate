import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class Team(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE,
    )
    point = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.character.name}-{self.point}'
