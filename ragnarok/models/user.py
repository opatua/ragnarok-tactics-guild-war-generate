import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords

from ragnarok.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, SafeDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(
        'Country',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
