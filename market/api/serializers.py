from rest_framework import serializers

from ..models import Market, Statistics


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = ('today_debt', 'debt_collection', 'debts', 'today_trade', 'trade')


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = "__all__"