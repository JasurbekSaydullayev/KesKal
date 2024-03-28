from rest_framework import viewsets
from rest_framework.response import Response

from ..models import Debtor
from .serializers import DebtorSerializer


class DebtorsModelViewSet(viewsets.ModelViewSet):
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        debtors = Debtor.objects.filter(market=user.market).all()
        return Response(debtors)

    def retrieve(self, request, *args, **kwargs):
        # debtors = Debtor.objects.filter()
        return Response({"message": "Method Not Allowed"}, status=405)

    def create(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def update(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)

    def delete(self, request, *args, **kwargs):
        return Response({"message": "Method Not Allowed"}, status=405)