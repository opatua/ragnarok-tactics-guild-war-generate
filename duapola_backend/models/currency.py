from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE
from simple_history.models import HistoricalRecords


class Currency(SafeDeleteModel):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=255)
    minor_unit = models.PositiveSmallIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='currencies_history')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'currencies'
