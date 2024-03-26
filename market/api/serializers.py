from rest_framework import serializers

from ..models import Market, Statistics


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = "__all__"


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = "__all__"