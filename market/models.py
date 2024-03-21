from django.db import models


class Market(models.Model):
    name = models.CharField(max_length=200)
    stir = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Statistics(models.Model):
    today_debt = models.DecimalField(max_digits=10, decimal_places=2)
    debt_collection = models.DecimalField(max_digits=10, decimal_places=2)
    debts = models.DecimalField(max_digits=10, decimal_places=2)
    today_trade = models.DecimalField(max_digits=10, decimal_places=2)
    trade = models.DecimalField(max_digits=10, decimal_places=2)
    market = models.OneToOneField(Market, on_delete=models.CASCADE, related_name='statistics')

    def __str__(self):
        return str(self.market)
