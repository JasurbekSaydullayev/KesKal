from rest_framework import serializers

from ..models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'price', 'comment', 'bar_code', 'created_at', 'market')
