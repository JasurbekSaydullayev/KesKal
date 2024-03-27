from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from users.models import User
from ..models import Products, Trade
from .serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'delete', 'put']
    permission_classes = [IsAuthenticated]
    lookup_field = 'bar_code'

    def list(self, request, *args, **kwargs):
        products = Products.objects.filter(market=request.user.market).all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        product = Products.objects.filter(bar_code=kwargs['bar_code'], market=request.user.market).all()
        serializer = ProductSerializer(product, many=True)
        if not serializer.data:
            return Response({"message": "Bunday mahsulot topilmadi"})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            product = Products.objects.filter(bar_code=serializer.validated_data['bar_code'],
                                              market=request.user.market).first()
            if product:
                return Response({"message": "Bunday mahsulot ushbu marketda oldin ro'yhatdan o'tgan"})
            serializer.validated_data['market'] = request.user.market
            serializer.save()
        return Response({"message": "ok"}, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        product = Products.objects.filter(bar_code=kwargs['bar_code'], market=request.user.market).first()
        if not product:
            return Response({"message": "Bunday mahsulot topilmadi"})
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        product = Products.objects.filter(bar_code=kwargs['bar_code'], market=request.user.market).first()
        if not product:
            return Response({"message": "Bunday mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({"message": "ok"}, status=status.HTTP_202_ACCEPTED)


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]
    lookup_field = 'phone_number'

