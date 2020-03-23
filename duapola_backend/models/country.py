from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords


class Country(SafeDeleteModel):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='countries_history')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'countries'
