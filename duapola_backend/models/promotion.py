import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords
from slugify import slugify


class Promotion(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='promotions_history')

    def __str__(self):
        return self.name

    def save(self, keep_deleted=False, **kwargs):
        self.slug = slugify(self.name)

        return super().save(keep_deleted=keep_deleted, **kwargs)

    class Meta:
        db_table = 'promotions'
