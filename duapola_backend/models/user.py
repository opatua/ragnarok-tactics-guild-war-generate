import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from safedelete.models import SafeDeleteModel
from simple_history.models import HistoricalRecords

from duapola_backend.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(table_name='users_history')

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'users'
