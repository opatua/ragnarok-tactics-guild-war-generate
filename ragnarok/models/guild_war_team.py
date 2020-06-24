import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class GuildWarTeam(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    guild_war = models.ForeignKey(
        'GuildWar',
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        'Team',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
