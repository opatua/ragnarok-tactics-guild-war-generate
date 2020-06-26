import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class SimulatorAttribute(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    simulator = models.ForeignKey(
        'Simulator',
        on_delete=models.CASCADE,
    )
    monster = models.ForeignKey(
        'Monster',
        on_delete=models.CASCADE,
    )
    essence = models.ForeignKey(
        'Essence',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
