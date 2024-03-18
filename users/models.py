import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from market.models import Market

User_Choice = (
    ('Director', 'Director'),
    ('Vendor', 'Vendor'),
)


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    type = models.CharField(max_length=25, choices=User_Choice)
    password = models.CharField(max_length=128)
    market = models.ForeignKey(Market, to_field='name', on_delete=models.CASCADE, related_name='user')
    is_confirmed = models.BooleanField(default=False)
    is_fired = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name
