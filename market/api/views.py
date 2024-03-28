from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import Statistics, Market
from .serializers import StatisticsSerializer, MarketSerializer


class StaticModelViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        statistics = Statistics.objects.filter(market=user.market).first()
        if statistics:
            serializer = self.get_serializer(statistics)
            return Response(serializer.data)
        else:
            return Response({"message": "Statistika topilmadi"}, status=404)

    def create(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def retrieve(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def update(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def delete(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)


class MarketModelViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
    http_method_names = ['get']
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def create(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def retrieve(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def update(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def delete(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)