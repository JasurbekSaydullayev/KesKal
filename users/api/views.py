from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from market.models import Market, Statistics
from ..models import User
from .serializers import UserSerializerForRegistration

from .validators import check_phone_number


class GetMethod(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerForRegistration

    def list(self, request, *args, **kwargs):
        user = list(User.objects.all().values())
        return Response(user)

    def retrieve(self, request, *args, **kwargs):
        data = list(User.objects.filter(id=kwargs['pk']).values())
        return Response(data)

    def create(self, request, *args, **kwargs):
        user_serializer_data = UserSerializerForRegistration(data=request.data)
        if user_serializer_data.is_valid(raise_exception=True):
            phone_number = user_serializer_data.validated_data['phone_number']
            if check_phone_number(phone_number) is None:
                return Response({"message": "Telefon raqam +998 dan boshlanishi, "
                                            "uzunligi 13 ta bo'lishi va raqamlardan tashkil topgan shart"},
                                status=status.HTTP_400_BAD_REQUEST)
            market = Market.objects.filter(name=user_serializer_data.validated_data['market'],
                                           stir=user_serializer_data.validated_data['stir']).first()
            # Userni tipini tekshiramiz
            if user_serializer_data.validated_data['type'] == "Director":
                # agar user tipi direktor bo'lsa ro'ythat o'tilishi
                # kutilayotgan marketning direktori bor yo'qligiga tekshiramiz
                if market is not None:
                    return Response({"message": "Ushbu marketda direktor allaqachon ro'yhatdan o'tgan"})
                else:
                    # agar hammasi to'g'ri kelsa market yaratamiz lekin saqlamaymiz
                    new_market = Market.objects.create(name=user_serializer_data.validated_data['market'],
                                                       stir=user_serializer_data.validated_data['stir'])
                    statistics = Statistics.objects.create(today_debt=0, debt_collection=0,
                                                           debts=0, today_trade=0, trade=0,
                                                           market=new_market)
                    statistics.save()
                    new_market.save()
                    user_serializer_data.validated_data['market'] = new_market
            elif user_serializer_data.validated_data['type'] == "Vendor":
                if market is None:
                    return Response({"message": "Bunday market mavjud emas"})
            else:
                return Response({"message": "Foydalanuvchi tipi no'to'g'ri kiritildi"},
                                status=status.HTTP_400_BAD_REQUEST)
            user_serializer_data.validated_data.pop('stir', None)
            phone_number = user_serializer_data.validated_data['phone_number']
            user_type = user_serializer_data.validated_data['type']
            first_name = user_serializer_data.validated_data['first_name']
            password = user_serializer_data.validated_data['password']
            if user_type == "Director":
                market = user_serializer_data.validated_data['market']
                user = User.objects.create(phone_number=phone_number, first_name=first_name, password=password,
                                           market=market, type=user_type, is_confirmed=True)
                user.save()
            elif user_type == "Vendor":
                user = User.objects.create(phone_number=phone_number, first_name=first_name, password=password,
                                           market=market, type=user_type)
                user.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "User Added Successfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Please fill the details correctly", "status": status_code})

    def update(self, request, *args, **kwargs):
        user_details = User.objects.get(id=kwargs['pk'])
        user_serializer_data = UserSerializerForRegistration(
            user_details, data=request.data, partial=True)
        if user_serializer_data.is_valid():
            user_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "User Updated Successfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "User data Not found", "status": status_code})
