import jwt
import uuid

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from django.contrib.auth.models import AbstractUser
from django.db import models

from market.models import Market
from .managers import UserManager

User_Choice = (
    ('Director', 'Director'),
    ('Vendor', 'Vendor'),
)


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True)
    type = models.CharField(max_length=25, choices=User_Choice)
    password = models.CharField(max_length=128)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='user', null=True,
                               blank=True)
    is_confirmed = models.BooleanField(default=False)
    is_fired = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'phone_number'
    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
