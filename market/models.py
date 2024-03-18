import uuid

from django.db import models


class Market(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Statistics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    today_debt = models.DecimalField(max_digits=10, decimal_places=2)
    debt_collection = models.DecimalField(max_digits=10, decimal_places=2)
    debts = models.DecimalField(max_digits=10, decimal_places=2)
    today_trade = models.DecimalField(max_digits=10, decimal_places=2)
    trade = models.DecimalField(max_digits=10, decimal_places=2)
    market = models.OneToOneField(Market, to_field='name', on_delete=models.CASCADE, related_name='statistics')

    def __str__(self):
        return self.market
