import uuid

from django.db import models
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords
from slugify import slugify


class Product(SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product_family = models.ForeignKey(
        'ProductFamily',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)
    quantity = models.IntegerField()
    currency = models.ForeignKey(
        'Currency',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=20,
        decimal_places=4,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='products_history')

    def __str__(self):
        return self.name

    def save(self, keep_deleted=False, **kwargs):
        self.slug = slugify(self.name)

        return super().save(keep_deleted=keep_deleted, **kwargs)

    class Meta:
        db_table = 'products'
