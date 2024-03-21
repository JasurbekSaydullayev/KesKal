from django.db import models
from market.models import Market


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(default="", null=True, blank=True)
    bar_code = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name
