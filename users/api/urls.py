from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router_user = DefaultRouter()
router_user.register('users', GetMethod, basename='users')

# urlpatterns = [
#     path('users/change-password/', ChangePasswordView.as_view(), name='change-password')
# ]

urlpatterns = router_user.urls


