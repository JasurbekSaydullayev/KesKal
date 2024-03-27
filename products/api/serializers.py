from rest_framework import serializers

from ..models import Products, Trade


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'price', 'comment', 'bar_code')


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ('product', 'user', 'created_at', 'market')
