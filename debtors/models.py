import uuid

from django.db import models
from market.models import Market
from users.models import User
from products.models import Products


class Debtor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, unique=True)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='debtors')
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='debtors')
    products = models.ManyToManyField(Products, related_name='debtors')

    def __str__(self):
        return self.full_name
