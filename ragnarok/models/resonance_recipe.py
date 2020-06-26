import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords

from ragnarok.enums import ElementEnum


class ResonanceRecipe(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    resonance = models.ForeignKey(
        'Resonance',
        on_delete=models.CASCADE,
    )
    element = models.CharField(
        max_length=255,
        choices=ElementEnum.choices(),
    )
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.resonance.name} - {self.element}'
