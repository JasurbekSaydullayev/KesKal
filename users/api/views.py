from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password

from market.models import Market, Statistics
from ..models import User
from .serializers import UserSerializerForRegistration

from .validators import check_phone_number


class GetMethod(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerForRegistration
    http_method_names = ['get', 'post']
    permission_classes = [IsAuthenticated]
    lookup_field = 'phone_number'

    def list(self, request, *args, **kwargs):
        user = request.user
        market = user.market
        if user.type == "Vendor":
            return Response({"message": "Sotuvchilarni ko'rish uchun ruxsat yo'q"})
        market_users = User.objects.filter(market=market)
        if market_users is None:
            return Response({"message": "Sizda sotuvchilar yo'q"})
        serializer = self.serializer_class(market_users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        data = list(User.objects.filter(phone_number=kwargs['phone_number']).values())
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
            if user_serializer_data.validated_data['type'] == "Director":
                check_stir_market = Market.objects.filter(stir=user_serializer_data.validated_data['stir']).first()
                if check_stir_market:
                    return Response({"message": "Bunday stirga ega market avval ro'yhatdan o'tgan"},
                                    status=status.HTTP_200_OK)
                if market is not None:
                    return Response({"message": "Ushbu marketda direktor allaqachon ro'yhatdan o'tgan"})
                else:
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
            password = make_password(user_serializer_data.validated_data['password'])
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


# class ChangePasswordView(APIView):
#     model = User
#     serializer_class = UserChangePasswordSerializer
#     http_method_names = ['post']
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             user = request.user
#             if not user.check_password(serializer.validated_data.get('old_password')):
#                 return Response({"error": "Invalid old password"}, status=status.HTTP_400_BAD_REQUEST)
#             user.set_password(serializer.validated_data.get('new_password'))
#             user.save()
#             return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
