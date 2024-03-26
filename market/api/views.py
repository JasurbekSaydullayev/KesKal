from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Market, Statistics
from .serializers import MarketSerializer, StatisticsSerializer


class MarketModelViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class StaticModelViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer